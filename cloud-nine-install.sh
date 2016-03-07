#!/bin/bash
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
export PATH="$HOME/miniconda/bin:$PATH"
conda install -q -y conda
conda update -q conda
conda create -y -n bw2 python=3.4
source activate bw2

conda install -q -y wheel
conda update -q wheel pip setuptools
conda install -y numpy ipython ipython-notebook jupyter matplotlib scipy flask lxml requests nose docopt whoosh xlsxwriter xlrd unidecode
pip install --no-cache-dir eight
pip install --no-cache-dir --pre brightway2

jupyter notebook --generate-config
echo 'c.NotebookApp.tornado_settings = {"headers": {"Content-Security-Policy": "frame-ancestors '\''self'\'' https://ide.c9.io "}}' >> /home/ubuntu/.jupyter/jupyter_notebook_config.py

echo '#!/bin/bash' > run_notebook.sh
echo 'export PATH="$HOME/miniconda/bin:$PATH"' >> run_notebook.sh
echo 'source activate bw2' >> run_notebook.sh
echo 'cd notebooks' >> run_notebook.sh
echo 'jupyter notebook --ip=0.0.0.0 --port=8080 --no-browser' >> run_notebook.sh
chmod +x run_notebook.sh

mkdir notebooks && cd notebooks
wget https://bitbucket.org/cmutel/brightway2/raw/default/notebooks/Getting%20Started%20with%20Brightway2.ipynb
jupyter notebook --ip $IP --port $PORT --no-browser
