import matplotlib.pyplot as plt


class TuringInit:
    mu_a = 0.00028
    mu_i = 0.005
    tau = 0.1
    k = -0.005
    size = 200
    dx = 0.01
    dy = 0.01
    T = 9
    dt = 0.001
    n = 9000

    @staticmethod
    def __get_all_attributes__(cls):
        attributes = {}
        for base_class in cls.__bases__:
            attributes.update(cls.__get_all_attributes__(base_class))
        attributes.update(vars(cls))
        return {
            k: v
            for k, v in attributes.items()
            if not k.startswith("__") and not callable(v)
        }

    def __str__(self):
        out = f"{self.__class__.__name__} model class:\n"
        for attr, val in self.__get_all_attributes__(self.__class__).items():
            out += f"\t{attr} = {self.__dict__.get(attr, val)}\n"
        return out

    @staticmethod
    def __plot_concentration__(C, ax):
        if len(C.shape) == 1:
            ax.plot(C, "-")
        elif len(C.shape) == 2:
            ax.imshow(C)
        elif len(C.shape) == 3:
            ax.imshow(C[..., -1])

    def plot_reactions(self, *, fig=None, ax=None):
        if hasattr(self, "A") or hasattr(self, "I"):
            if fig is None and ax is None:
                fig, ax = plt.subplots()
            elif fig is None:
                fig = ax.get_figure()
            if ax is None:
                ax = fig.add_subplot(111)
        else:
            print(
                "Please compute `A` or `I` and store them in `self.A` and `self.I`"
                "before running that method"
            )
            return

        if hasattr(self, "A"):
            self.__plot_concentration__(self.A, ax)
        if hasattr(self, "I") and not 2 < len(self.I.shape):
            self.__plot_concentration__(self.I, ax)
        fig.tight_layout()

    def __init__(self, **kwargs):
        for arg_name, arg_val in kwargs.items():
            if hasattr(self, arg_name):
                self.__dict__[arg_name] = arg_val
