<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<div align="center">
    <h2 style="font-size: 50px; font-weight: bold; margin: 0px;">
        Homography Estimation
    </h2>
    <h2 style="font-size: 30px; margin: 0px;">
        Dean Stratakos
    </h2>
    A RANSAC algorithm to estimate homographies between consecutive image
    frames.
    <br />
    <a href="https://github.com/dastratakos/Homography-Estimation">
        Explore the docs
    </a>
    ·
    <a href="https://github.com/dastratakos/Homography-Estimation/issues">
        Request Feature
    </a>
</div>

<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Functionality](#functionality)
  * [Algorithm details](#algorithm-details)
  * [Examples](#examples)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Future Work](#future-work)
* [License](#license)
* [Contact](#contact)

<!-- ABOUT THE PROJECT -->
## About the Project

### Functionality

This project currently has two main features.

The first functionality is to estimate a homography between two input image
frames. This is achieved by finding key points in each image, finding key point
matches between the images, and running RANSAC to determine inliers and
outliers in the matches.

The second functionality is to extend the first feature to operate over an
entire sequence of frames, or an input video. This outputs a new video
highlighting inliers and outliers across frames as well as homographies
relating each pair of consecutive frames.

<hr align="left" width="50%" style="margin-left: 15px">

### Algorithm details

<b>Homographies</b>

In computer vision, a homography is a transformation that describes the
relationship between any two images (or photographs) of the same plane in
space. More mathematically (in projective geometry), a homography is an
isomorphism of projective spaces, and have been historically used to explain
and study the difference in appearance of two planes observed from different
points of view. Homographies can be represented as a 3 x 3 matrix which can be
left-multiplied with any homogeneous point in the original image to describe
where that point lies in the transformed image.

Applications of homographies include removing perspective distortion (computer
vision), rendering textures (computer graphics), and computing planar shadows
(computer graphics). In this project, homographies are used to compute the
camera motion - namely the rotation and translation - between two images.

<b>RANSAC algorithm</b>

The RANdom SAmple Consensus (RANSAC) algorithm is a general parameter
estimation approach to compensate for a large proportion of outliers in the
data. In this application, the input data to RANSAC is the collection of
keypoint matches between consecutive frames, and the algorithm picks out
matches which are true matches (inliers) versus false matches (outliers).

Algorithm (from http://www.cse.yorku.ca/~kosta/CompVis_Notes/ransac.pdf):
1. Select randomly the minimum number of points required to determine the model
parameters.
2. Solve for the parameters of the model.
3. Determine how many points from the set of all points fit with a predefined
tolerance ε.
4. If the fraction of the number of inliers over the total number points in the
set exceeds a predefined threshold τ, re-estimate the model parameters using
all the identified inliers and terminate.
5. Otherwise, repeat steps 1 through 4 (maximum of N times).

Since a homography can be computed from just 4 tie points, step 1 requires
randomly choosing 4 tie points between the images.

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

<!-- FUTURE WORK -->
## Future Work

- [ ] Reformat output of video analysis to collect homographies for each pair
of consecutive frames in a CSV or JSON file.
- [ ] In video analysis, use the estimated homographies to create a "tripod
stabilization" effect.
- [ ] Fine tune inlier/outlier points.

See the [open issues](https://github.com/dastratakos/Homography-Estimation/issues)
for a more detailed list of proposed features (and known issues).

<!-- LICENSE -->
## License

Distributed under the Apache 2.0 License. See the [`LICENSE`](LICENSE) for more information.

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
