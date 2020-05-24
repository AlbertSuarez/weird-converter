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

🔀 Strange combinations converter like from Audio to Image

## Installation

Install client via pip. Ideally, `weird-converter` is well supported for Python >= 3.7.

```bash
pip3 install weird-converter
```

## Usage

Just run it like this:

```python
weird_converter.audio_to_image('audio.wav')  # It only supports wav files, for now.
```

## Future development

* 🎶 Support other input audio types.
* 📷 Implement image to audio conversion.
* 📹 Implement audio to video conversion (and the same other way around).

## Results

### Audio to image

From this [fanfare audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/fanfare.wav) to this image:

<p align="center">
  <img alt="Fanfare image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/fanfare.png" width="30%"/>
</p>

Or from this [empty audio](https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/silent.wav), representing a silence, to this image:

<p align="center">
  <img alt="Silent image" src="https://raw.githubusercontent.com/AlbertSuarez/weird-converter/master/examples/from_audio/silent.png" width="30%"/>
</p>

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
