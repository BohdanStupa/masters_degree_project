import argparse
from pathlib import Path

from mumford_shah import mumford_shah


def main(parser: argparse.ArgumentParser) -> None:
    args = parser.parse_args()
    n_iter: int = args.n_iter
    lmbda: float = args.lmbda
    theta: float = args.theta
    tau: float = args.tau
    h: float = args.hh
    n_clasters: int = args.n_clasters
    input_image_path: str = args.input_image_path
    mumford_shah(Path(input_image_path), n_iter, lmbda, theta, tau, h, n_clasters)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'input_image_path',
        type=str,
        help='input image'
    )
    parser.add_argument(
        '-n_iter',
        default=10,
        type=int,
    )
    parser.add_argument(
        '-lambda',
        default=1.,
        dest='lmbda',
        type=float,
        help='Regulaization term. Lower means smoother, higher means closer to image'
    )
    parser.add_argument(
        '-theta',
        default=1.,
        type=float,
    )
    parser.add_argument(
        '-tau',
        default=0.05,
        type=float,
    )
    parser.add_argument(
        '-hh',
        default=1.,
        type=float,
    )
    parser.add_argument(
        '-n_clasters',
        default=7,
        type=int,
    )
    parser.add_argument(
        '-update_progress_frequency',
        default=0,
        type=int,
    )
    main(parser)

