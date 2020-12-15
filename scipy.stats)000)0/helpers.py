import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
from scipy.stats import rv_continuous as rv_class
from typing import List


class normstep(rv_class):
    """
    A class for a distribution which density is something weird.
    I know it is non-informative just don't know what is this docstring for.

    Methods overwritten:
    _pdf,
    _rvs.
    """

    def pdf(
        self, x: List[int], left_scale: float, right_scale: float, exp: float
    ) -> np.array:
        """
        A pdf func for the weirdo.

        Kwargs:
        exp: expected middle of the weird distribution,
        left_scale: scaling the normal part of distr,
        right_scale: scaling the uniform part of distr.
        """

        # Oh shit I'm sorry for this.
        left_array = [*filter(lambda y: y < exp, x)]
        right_array = [*filter(lambda y: y >= exp, x)]

        # I know it hurts.
        left_side = st.norm(loc=exp, scale=left_scale).pdf(left_array)
        right_side = st.uniform(loc=exp, scale=right_scale).pdf(right_array)
        return np.append(left_side, 0.5 * right_side)

    def rvs(self, left_scale: float, right_scale: float, exp: float) -> np.array:
        """
        An rvs func for the weirdo.

        Kwargs:
        exp: expected middle of the weird distribution,
        left_scale: scaling the normal part of distr,
        right_scale: scaling the uniform part of distr.
        """

        uniform_rvs = st.uniform(loc=0, scale=1).rvs()

        return np.where(
            uniform_rvs > 0.5,
            -abs(st.norm(loc=exp, scale=left_scale).rvs()),
            st.uniform(loc=exp, scale=right_scale).rvs(),
        )


if __name__ == "__main__":
    n_step = normstep(name="normstep")
    x = list(np.arange(-3, 3, step=0.01))
    y = n_step.pdf(x, left_scale=1, right_scale=1.25, exp=0)
    print(y)
