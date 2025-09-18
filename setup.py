import setuptools
from pathlib import Path

HERE = Path(__file__).parent
README = (HERE / "README.md").read_text(encoding="utf-8") if (HERE / "README.md").exists() else ""

setuptools.setup(
    name="tts_webui_extension.demucs",
    packages=setuptools.find_namespace_packages(),
    version="0.0.4",
    author="rsxdalv",
    description="Demucs is a music source separation model that can separate drums, bass, vocals, and other instruments",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/rsxdalv/tts_webui_extension.demucs",
    project_urls={},
    scripts=[],
    install_requires=[
        "demucs",
        "torchaudio>=2.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

