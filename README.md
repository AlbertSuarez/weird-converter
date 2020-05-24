# Weird converter

[![PyPI version](https://badge.fury.io/py/weird-converter.svg)](https://pypi.org/project/weird-converter/)
[![Downloads](https://pepy.tech/badge/weird-converter)](https://pepy.tech/project/weird-converter)
[![Downloads](https://pepy.tech/badge/weird-converter/month)](https://pepy.tech/project/weird-converter/month)
[![Downloads](https://pepy.tech/badge/weird-converter/week)](https://pepy.tech/project/weird-converter/week)
<br>
[![HitCount](http://hits.dwyl.io/AlbertSuarez/weird-converter.svg)](http://hits.dwyl.io/AlbertSuarez/weird-converter)
![Python package](https://github.com/AlbertSuarez/weird-converter/workflows/Python%20package/badge.svg)
[![codecov](https://codecov.io/gh/AlbertSuarez/weird-converter/branch/master/graph/badge.svg)](https://codecov.io/gh/AlbertSuarez/weird-converter)
[![GitHub stars](https://img.shields.io/github/stars/AlbertSuarez/weird-converter.svg)](https://GitHub.com/AlbertSuarez/weird-converter/stargazers/)
[![GitHub forks](https://img.shields.io/github/forks/AlbertSuarez/weird-converter.svg)](https://GitHub.com/AlbertSuarez/weird-converter/network/)
[![GitHub contributors](https://img.shields.io/github/contributors/AlbertSuarez/weird-converter.svg)](https://GitHub.com/AlbertSuarez/weird-converter/graphs/contributors/)

🔀 Strange combinations converter like from Audio to Image and Image to Audio

## Installation

Install client via pip. Ideally, `weird-converter` is well supported for Python >= 3.7.

```bash
pip3 install weird-converter
```

## Usage

Just run it like this:

```python
weird_converter.audio_to_image('audio.wav')  # It only supports wav files, for now.
weird_converter.image_to_audio('image.jpg')
```

## Future development

* 🎶 Support other input audio types.
* 📹 Implement audio to video conversion (and the same other way around).
* ⭐️ Implement custom transformations for getting different results.

## Motivation

I know this tool is kind of strange and probably not very useful. However, I wanted to play with numpy and try to understand in a deeper way the amount of stuff that this library can do. That's why I ended up doing this project where I see a lot of progression with different future tweakments (as it is specified above).

## Results

### Audio to image

Image generation comes from a normalization of the audio values. The image will have higher dimensions as more information the audio has, like audio length or channels available.

From this [fanfare audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/fanfare.wav) to this image:

<p align="center">
  <img alt="Fanfare image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/fanfare.jpg" width="30%"/>
</p>

Or from this [empty audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/silent.wav), representing a silence, to this image:

<p align="center">
  <img alt="Silent image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/silent.jpg" width="30%"/>
</p>
### Image to Audio

Audio generation comes from a normalization to a 44,100 samples per second audio. The output length will be higher depending on the dimensions of the input image. As you could check, the results look very similar to an helicopter sound but it differs depending on the given image.

<p align="center">
  <img alt="Church image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_image/church.jpg" width="30%"/>
</p>

To this [audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_image/church.wav), where it's clear when the audio is playing the black background and the building pixels.

<p align="center">
  <img alt="Black image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_image/black.jpg" width="30%"/>
</p>

To this near empty [audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_image/black.wav) and very uniform.

## Development

### Recommendations

Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

### Installation

1. Setup virtual environment

2. Install dependencies

  ```bash
  pip3 install -r requirements.lock
  ```

3. Install locally

  ```bash
  pip3 install .
  ```

## Contributing

Suggestions, improvements, and enhancements are always welcome! If you have any issues, please do raise one in the Issues section. If you have an improvement, do file an issue to discuss the suggestion before creating a PR.

All ideas – no matter how outrageous – welcome!

## Authors

- [Albert Suàrez](https://github.com/AlbertSuarez)

## License

Apache-2.0 © weird-converter
