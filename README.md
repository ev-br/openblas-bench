# Continuous benchmarking of OpenBLAS performance

Run periodically a set of benchmarks for low-level OpenBLAS primitives.

## Benchmark runner

[![CodSpeed Badge](https://img.shields.io/endpoint?url=https://codspeed.io/badge.json)](https://codspeed.io/ev-br/openblas-bench)

We rely on codspeed.io, which runs things on CI. Here is the dashboard: https://codspeed.io/ev-br/openblas-bench/

Click on [benchmarks](https://codspeed.io/ev-br/openblas-bench/benchmarks) to see the performance of a particular benchmark over time;
Click on [branches](https://codspeed.io/ev-br/openblas-bench/branches/) and then on the last PR link to see the flamegraphs.

## Running benchmarks locally

The benchmark syntax is consistent with that of `pytest-benchmark` framework. Thus the incantation is `$ pytest pytest_benchmarks/test_blas.py`.
An ASV compatible benchmark suite is planned but currently not implemented.

## Which OpenBLAS

We install the nightly builds of `scipy_openblas32` from the [scientific python staging bucket](https://anaconda.org/scientific-python-nightly-wheels/scipy-openblas32).
The particular OpenBLAS version is reported by the [CI workflow](https://github.com/ev-br/openblas-bench/blob/main/.github/workflows/codspeed.yml#L28).

## What are the benchmarks

We run raw BLAS/LAPACK subroutines, via f2py-generated python wrappers. The wrappers themselves are equivalent to [those from SciPy](https://docs.scipy.org/doc/scipy/reference/linalg.lapack.html).
In fact, the wrappers _are_ from SciPy, we only adjust the routine names to follow the `scipy_openblas32` convention: `dgesdd` becomes `scipy_dgesdd` and so on.
We build our wrappers in this repository however, simply to avoid having to build the whole SciPy for each CI run.

## Where is what

- `.github/workflows/codspeed.yml` does all the orchestration
- benchmarks themselves live in the `pytest_benchmarks` folder. Note that the LAPACK routines are imported from the `openblas_wrap` package.
- the `openblas_wrap` package is a simple trampoline: it contains an f2py extension, `_flapack`, which talks to OpenBLAS, and exports the python names in its `__init__.py`.
This way, the `openblas_wrap` package shields the benchmarks from the details of where a particular LAPACK function comes from. If wanted, you may for instance swap the `_flapack` extension to
`scipy.linalg.blas` and `scipy.linalg.lapack`.
