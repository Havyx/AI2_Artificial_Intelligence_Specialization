
### Adicionar ambiente conda ao Kernel do Jupyter
https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084  
```
conda create --name firstEnv
```
```
conda install -c conda-forge tensorflow
```
```
conda install -c anaconda ipykernel
```
```
python -m ipykernel install --user --name=firstEnv 
```  
Using the above command, I will now have this conda environment in my Jupyter notebook. 
  
### Remover Kernel do Jupyter
https://stackoverflow.com/questions/42635310/remove-kernel-on-jupyter-notebook  
```
jupyter kernelspec list
```
```
jupyter kernelspec uninstall unwanted-kernel
```  
* Problemas: Dead Kernel Python 3 -> Solucao foi remover o kernel Python 3 e automaticamente o anaconda criou um outro válido.