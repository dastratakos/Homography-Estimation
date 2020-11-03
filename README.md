<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<p align="center">
  <h2 align="center" style="font-size: 50px; font-weight: bold; margin: 0px;">Homography Estimation</h2>
  <h2 align="center" style="font-size: 30px; margin: 0px;">Dean Stratakos</h2>
  <p align="center">
    A RANSAC algorithm to estimate homographies between consecutive image frames.
    <br />
    <a href="https://github.com/dastratakos/Homography-Estimation">Explore the docs</a>
    ·
    <a href="https://github.com/dastratakos/Homography-Estimation">View Demo</a>
    ·
    <a href="https://github.com/dastratakos/Homography-Estimation/issues">Request Feature</a>
  </p>
</p>

<!-- <hr> -->

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Examples](#examples)
  * [Functionality](#functionality)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)

<!-- <hr> -->

<!-- ABOUT THE PROJECT -->
## About The Project

From Wikipedia: [Homography (computer vision)](https://en.wikipedia.org/wiki/Homography_(computer_vision))

In the field of computer vision, any two images of the same planar surface in
space are related by a homography (assuming a pinhole camera model). This has
many practical applications, such as image rectification, image registration,
or computation of camera motion—rotation and translation—between two images.
Once camera rotation and translation have been extracted from an estimated
homography matrix, this information may be used for navigation, or to insert
models of 3D objects into an image or video, so that they are rendered with the
correct perspective and appear to have been part of the original scene
(see Augmented reality).

<hr align="left" width="50%" style="margin-left: 15px">

### Functionality

This project has two features so far. First, it can estimate a homography
between two input image frames. Second, it extends this functionality to
operate over a sequence of frames, or an input video.

<hr align="left" width="50%" style="margin-left: 15px">

### Examples
<div align="center">
    <div style="display: inline-block">
        <div style:after="content: ''; display: table; clear: both;">
            <div style="float: left; width: 50%;">
                <p>Input images</p>
                <div style="padding: 10px;">
                    <img src="examples/images/02/1.png" alt="Input image 1" height="200"/>
                    <img src="examples/images/02/2.png" alt="Input image 2" height="200"/>
                </div>
            </div>
            <div style="float: left; width: 50%;">
                <p>Identify keypoints</p>
                <div style="padding: 10px;">
                    <img src="examples/images/02/keypoints-1.png" alt="Keypoints of image 1" height="200"/>
                    <img src="examples/images/02/keypoints-2.png" alt="Keypoints of image 2" height="200"/>
                </div>
            </div>
        </div>
        </br>
        <div style:after="content: ''; display: table; clear: both;">
            <div style="float: left; width: 50%;">
                <p>Determine matches</p>
                <img src="examples/images/02/matches.png" alt="Keypoint matching" height="200" style="padding: 10px;"/>
            </div>
            <div style="float: left; width: 50%;">
                <p>Use RANSAC to find inliers (green) & outliers (red)</p>
                <img src="examples/images/02/inlier_matches.png" alt="Inliers and outliers" height="200" style="padding: 10px;"/>
            </div>
        </div>
        Estimated Homography:
        <table>
            <tr>
                <td style="border: 1px solid black;">1.00000000e+00</td>
                <td style="border: 1px solid black;">-1.84873558e-12</td>
                <td style="border: 1px solid black;">2.91736753e-09</td>
            </tr>
            <tr>
                <td style="border: 1px solid black;">2.39456865e-12</td>
                <td style="border: 1px solid black;">1.00000000e+00</td>
                <td style="border: 1px solid black;">-1.08356205e-08</td>
            </tr>
            <tr>
                <td style="border: 1px solid black;">1.20185168e-15</td>
                <td style="border: 1px solid black;">-5.76888806e-16</td>
                <td style="border: 1px solid black;">1.00000000e+00</td>
            </tr>
        </table>
        <br />
    </div>
</div>

<hr width="75%">

<div align="center">
    <div style="display: inline-block">
        <p>Input and output video</p>
        <img src="examples/videos/02/video-input.gif" alt="Input video" width="400" style="padding: 10px;"/>
        <img src="examples/videos/02/video-RANSAC.gif" alt="RANSAC example video" width="400" style="padding: 10px;"/>
    </div>
</div>

<!-- <hr> -->

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

<hr align="left" width="50%" style="margin-left: 15px">

### Prerequisites

* [Python 3.7.9](https://www.python.org/downloads/release/python-379/)
* [OpenCV](https://opencv.org)
* [NumPy](https://numpy.org)
* [MoviePy](https://pypi.org/project/moviepy/)

<hr align="left" width="50%" style="margin-left: 15px">

### Installation

1. Clone the repo
```sh
git clone https://github.com/dastratakos/Homography-Estimation.git
```
2. Add images and videos. Images should go in the directory `input/images/[dir]`
and videos should go in the directory `input/videos/[dir]`, where `[dir]` is a
2 digit unique identifier within either directory.

<!-- <hr> -->

<!-- USAGE EXAMPLES -->
## Usage

1. Here is an example of running homography estimation on two image frames,
which are stored as `input/images/01/1.png` and `input/images/01/2.png`.
```sh
python imageAnalysis.py -d 01
```
2. This is an example of running homography estimation on a full video, which
is stored as `input/videos/02/IMG_1554.MOV`.
```sh
python videoAnalysis.py -d 02
```

<!-- <hr> -->

<!-- ROADMAP -->
## Roadmap

* In video analysis, use the estimated homographies to create a "tripod
stabilization" effect.
* Fine tune inlier/outlier points.

See the [open issues](https://github.com/dastratakos/Homography-Estimation/issues)
for a more detailed list of proposed features (and known issues).

<!-- <hr> -->

<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See the [`LICENSE`](LICENSE) for more information.

<!-- <hr> -->

<!-- CONTACT -->
## Contact

Dean Stratakos - [dstratak@stanford.edu](mailto:dstratak@stanford.edu)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/dastratakos/Homography-Estimation.svg?style=flat-square
[contributors-url]: https://github.com/dastratakos/Homography-Estimation/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/dastratakos/Homography-Estimation.svg?style=flat-square
[forks-url]: https://github.com/dastratakos/Homography-Estimation/network/members
[stars-shield]: https://img.shields.io/github/stars/dastratakos/Homography-Estimation.svg?style=flat-square
[stars-url]: https://github.com/dastratakos/Homography-Estimation/stargazers
[issues-shield]: https://img.shields.io/github/issues/dastratakos/Homography-Estimation.svg?style=flat-square
[issues-url]: https://github.com/dastratakos/Homography-Estimation/issues
[license-shield]: https://img.shields.io/github/license/dastratakos/Homography-Estimation.svg?style=flat-square
[license-url]: https://github.com/dastratakos/Homography-Estimation/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/dean-stratakos-8b338b149