.. image:: https://img.shields.io/github/license/felixriese/hyperspectral-regression
    :target: LICENSE
    :alt: License: BSD-3-Clause

.. image:: https://mybinder.org/badge_logo.svg
    :target: https://mybinder.org/v2/gh/felixriese/hyperspectral-regression/master?filepath=notebooks
    :alt: MyBinder

.. image:: https://travis-ci.org/felixriese/hyperspectral-regression.svg?branch=master
    :target: https://travis-ci.org/felixriese/hyperspectral-regression
    :alt: Travis.CI Status

.. image:: https://codecov.io/gh/felixriese/hyperspectral-regression/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/felixriese/hyperspectral-regression
    :alt: Codecov

.. image:: https://api.codacy.com/project/badge/Grade/6808eea2d5984c7d8364f7659b40f9ea
    :target: https://www.codacy.com/manual/felixriese/hyperspectral-regression?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=felixriese/hyperspectral-regression&amp;utm_campaign=Badge_Grade
    :alt: Codacy Status

Hyperspectral Regression: Code Examples
===============================================

This repository consists of additional material and exemplary implementations for a coming book chapter.

The code in this repository is provided via notebooks. The notebooks are structured as follows:

1. `Data <notebooks/1_Data.ipynb>`_
2. `Features <notebooks/2_Features.ipynb>`_
3. `Supervised Learning <notebooks/3_Supervised_Learning.ipynb>`_
4. `Active Learning <notebooks/4_Active_Learning.ipynb>`_
5. `Model Selection and Evaluation <notebooks/5_Model_Selection_and_Evaluation.ipynb>`_
6. `Generative Adversarial Networks <notebooks/6_GANs.ipynb>`_

Description
-----------



:License:
    `3-Clause BSD license <LICENSE>`_

:Authors:
    `Felix M. Riese <mailto:github@felixriese.de>`_, `Sina Keller <mailto:sina.keller@kit.edu>`_

:Citation:
    see `Citation`_

:Paper:
    `Riese and Keller (2020) <https://doi.org/10.1007/978-3-030-38617-7_7>`_

:Requirements:
    Python 3 with these `packages <requirements.txt>`_


How to use this repository?
---------------------------

1. Install Python 3, e.g. with `Anaconda <https://www.anaconda.com/distribution/>`_

2. Install the required packages

    conda install --file requirements.txt

3. Start jupyter

    jupyter notebook

4. Open the notebook folder in this repository in the Jupyter browser and select the desired notebook.

---

Citation
--------

The bibtex file including both references is available in `bibliography.bib
<bibliography.bib>`_.

**Paper:**

Felix M. Riese and Sina Keller, "Supervised, Semi-Supervised, and Unsupervised
Learning for Hyperspectral Regression", in *Hyperspectral Image Analysis:
Advances in Machine Learning and Signal Processing*, Saurabh Prasad and Jocelyn
Chanussot, Eds. Cham: Springer International Publishing, 2020, ch. 7,
pp. 187–232.

.. code:: bibtex

    @incollection{riese2020supervised,
        author = {Riese, Felix~M. and Keller, Sina},
        title ={{Supervised, Semi-Supervised, and Unsupervised Learning for
                Hyperspectral Regression}},
        booktitle = {{Hyperspectral Image Analysis: Advances in Machine
                     Learning and Signal Processing}},
        editor = {Prasad, Saurabh and Chanussot, Jocelyn},
        year = {2020},
        publisher = {Springer International Publishing},
        address = {Cham},
        chapter = {7},
        pages = {187--232},
        doi = {10.1007/978-3-030-38617-7_7},
    }

**Code:**

Felix M. Riese and Sina Keller, "Hyperspectral Regression: Code Examples",
Zenodo, `10.5281/zenodo.3450676 <http://doi.org/10.5281/zenodo.3450676>`_,
2019.

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3450676.svg
    :target: https://doi.org/10.5281/zenodo.3450676
    :alt: DOI

.. code:: bibtex

    @misc{riese2019hyperspectral,
        author = {Riese, Felix~M. and Keller, Sina},
        title = {{Hyperspectral Regression: Code Examples}},
        year = {2019},
        DOI = {10.5281/zenodo.3450676},
        publisher = {Zenodo},
        howpublished = {\href{https://doi.org/10.5281/zenodo.3450676}{doi.org/10.5281/zenodo.3450676}}
    }
