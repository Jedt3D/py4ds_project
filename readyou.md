# Read Me 6409035752

รายชื่อ libraries สำหรับงาน data science __ทดสอบมาบน Python 3.11__ สำหรับ macOS 13 แต่ควรใช้ได้กับ Python 3.11 บน platform อื่นๆ ไม่ยากนัก

1. สร้าง virtualenv ก่อนใช้งานเสมอ
2. ติดตั้ง libraryเหล่านี้ด้วยคำสั่งด้านล่าง

> pip install -r requirements.txt

3. ต้องติดตั้ง PyTest ให้ project ตามวิดีโอนี้

![PyTest Setup](./setup_pytest_in_project.gif)

4. เซ็ตค่า Label folder ให้เป็น src/, tests/ 

![Label Folders](./label_folder.jpeg)
-----
### รายชื่อ library และ version (2023-10-01)

```
alabaster==0.7.13
anyio==4.0.0
appnope==0.1.3
argon2-cffi==23.1.0
argon2-cffi-bindings==21.2.0
arrow==1.2.3
asttokens==2.4.0
async-lru==2.0.4
attrs==23.1.0
Babel==2.12.1
backcall==0.2.0
beautifulsoup4==4.12.2
black==23.9.1
bleach==6.0.0
certifi==2023.7.22
cffi==1.16.0
charset-normalizer==3.3.0
click==8.1.7
comm==0.1.4
contourpy==1.1.1
coverage==7.3.1
cycler==0.12.0
Cython==3.0.2
debugpy==1.8.0
decorator==5.1.1
defusedxml==0.7.1
docutils==0.20.1
executing==2.0.0
fastjsonschema==2.18.0
fonttools==4.43.0
fqdn==1.5.1
idna==3.4
imageio==2.31.4
imagesize==1.4.1
iniconfig==2.0.0
ipykernel==6.25.2
ipython==8.16.0
ipywidgets==8.1.1
isoduration==20.11.0
jedi==0.19.0
Jinja2==3.1.2
joblib==1.3.2
json5==0.9.14
jsonpointer==2.4
jsonschema==4.19.1
jsonschema-specifications==2023.7.1
jupyter-events==0.7.0
jupyter-lsp==2.2.0
jupyter_client==8.3.1
jupyter_core==5.3.2
jupyter_server==2.7.3
jupyter_server_terminals==0.4.4
jupyterlab==4.0.6
jupyterlab-pygments==0.2.2
jupyterlab-widgets==3.0.9
jupyterlab_server==2.25.0
kiwisolver==1.4.5
lazy_loader==0.3
MarkupSafe==2.1.3
matplotlib==3.8.0
matplotlib-inline==0.1.6
mistune==3.0.2
mypy==1.5.1
mypy-extensions==1.0.0
nbclient==0.8.0
nbconvert==7.8.0
nbformat==5.9.2
nest-asyncio==1.5.8
networkx==3.1
notebook==7.0.4
notebook_shim==0.2.3
numpy==1.26.0
numpydoc==1.6.0
overrides==7.4.0
packaging==23.1
pandas==2.1.1
pandocfilters==1.5.0
parso==0.8.3
pathspec==0.11.2
pexpect==4.8.0
pickleshare==0.7.5
Pillow==10.0.1
platformdirs==3.10.0
plotly==5.17.0
pluggy==1.3.0
pooch==1.7.0
prometheus-client==0.17.1
prompt-toolkit==3.0.39
psutil==5.9.5
ptyprocess==0.7.0
pure-eval==0.2.2
pycparser==2.21
Pygments==2.16.1
pyparsing==3.1.1
pytest==7.4.2
pytest-cov==4.1.0
python-dateutil==2.8.2
python-json-logger==2.0.7
pytz==2023.3.post1
PyWavelets==1.4.1
PyYAML==6.0.1
pyzmq==25.1.1
referencing==0.30.2
requests==2.31.0
rfc3339-validator==0.1.4
rfc3986-validator==0.1.1
rpds-py==0.10.3
ruff==0.0.291
scikit-image==0.21.0
scikit-learn==1.3.1
scipy==1.11.3
seaborn==0.13.0
Send2Trash==1.8.2
six==1.16.0
sniffio==1.3.0
snowballstemmer==2.2.0
soupsieve==2.5
Sphinx==7.2.6
sphinx-copybutton==0.5.2
sphinx-gallery==0.14.0
sphinx-prompt==1.8.0
sphinxcontrib-applehelp==1.0.7
sphinxcontrib-devhelp==1.0.5
sphinxcontrib-htmlhelp==2.0.4
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.6
sphinxcontrib-serializinghtml==1.1.9
sphinxext-opengraph==0.8.2
stack-data==0.6.3
tabulate==0.9.0
tenacity==8.2.3
terminado==0.17.1
threadpoolctl==3.2.0
tifffile==2023.9.26
tinycss2==1.2.1
tornado==6.3.3
traitlets==5.10.1
typing_extensions==4.8.0
tzdata==2023.3
uri-template==1.3.0
urllib3==2.0.5
wcwidth==0.2.8
webcolors==1.13
webencodings==0.5.1
websocket-client==1.6.3
widgetsnbextension==4.0.9
```