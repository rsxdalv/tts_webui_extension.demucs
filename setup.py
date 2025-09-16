import setuptools

setuptools.setup(
    name="tts_webui_extension.demucs",
    packages=setuptools.find_namespace_packages(),
    version="0.0.3",
    author="rsxdalv",
    description="Demucs is a music source separation model that can separate drums, bass, vocals, and other instruments",
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

