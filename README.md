# Notes
Anotacoes gerais / Link de sites  

https://towardsdatascience.com/best-clustering-algorithms-for-anomaly-detection-d5b7412537c8  
https://medium.com/@elutins/dbscan-what-is-it-when-to-use-it-how-to-use-it-8bd506293818  

https://www.howtoforge.com/tutorial/install-git-and-github-on-ubuntu/  

https://www.gitignore.io/

https://blog.pythonanywhere.com/169/

https://blog.pythonanywhere.com/121/

### Selecionar Ambientes no Jupyter  
conda install jupyter
conda install nb_conda
conda install ipykernel
python -m ipykernel install --user --name mykernel

jupyter kernelspec remove mykernel

www.ni.com/myni/dashboard
login: jorge.mondadori@sistemafiep.org.br
senha: 12345678
Serial LabView: M84X16318  

848 367 8089

https://towardsdatascience.com/coding-ml-tools-like-you-code-ml-models-ddba3357eace    
  
git branch  
git branch nome_do_branch   
git checkout nome_do_branch  
...  
git push  
git checkout master  
git pull  
git merge nome_do_branch  
git push  
git fetch --all    
git reset --hard origin/master    
  
pandas where loc mask good examples:
https://kanoki.org/2019/07/17/pandas-how-to-replace-values-based-on-conditions/  
  
https://amitkushwaha.co.in/data-visualization-part-1.html  
  
https://www.kaggle.com/masumrumi/a-statistical-analysis-ml-workflow-of-titanic  
  
https://blog.minitab.com/blog/understanding-statistics/understanding-qualitative-quantitative-attribute-discrete-and-continuous-data-types  
  
Empresa: nuveo -> Visao computacional com funil de pre processamento
* Ultra OCR  
  
https://www.ultraocr.com.br/
  Orizon Leitura de Guias Medicas
  
  selenium

### Hard code python RPA
  pytorch
  opencv
  azure,aws -> engine pronto NA
  entrega da engine -> entrega de IA
 --------------------------------------------------------------------------------------------
 #### SELENIUM
  Adicionar executavel geckodriever ao path:  
  
  export PATH=$PATH:/root/pasta.
  
  https://medium.com/@cagriaydogdu2334/3d-visualization-of-k-means-clustering-47d3d3e82117
  
  https://www.bigendiandata.com/2017-04-18-Jupyter_Customer360/   
  
 http://scraping.pro/recaptcha-solve-selenium-python/  
 
   https://www.howtoforge.com/tutorial/tesseract-ocr-installation-and-usage-on-ubuntu-16-04/  
   --------------------------------------------------------------------------------------------
### Listagem de tecnologias a serem estudadas  
1.


u executei com sucesso esta solução abaixo para o meu problema:

    Na BIOS, altere a Boot Sequence para permitir a inicialização via USB (contendo o Ubuntu)

    No GRUB, selecione Experimente o Ubuntu sem instalar

    Uma vez no Ubuntu, pressione Ctrl + Alt + T para abrir o Terminal

    Digite sudo efibootmgr para listar todas as entradas no Menu de inicialização

    Encontre Ubuntu no menu e anote o número de inicialização, por exemplo, Boot0001

    Digite sudo efibootmgr -b 1 -B para excluir a entrada do Menu de inicialização

-b : modificar o número de inicialização -B : excluir o número de inicialização

Depois disso, tudo o que fiz foi mudar o Gerenciador de inicialização do Windows para o topo do menu de inicialização > voltar para o Windows 10 > Crie e formate partições do disco rígido e estenda a partição do meu Windows C:\ Drive para mesclar com o espaço livre de onde veio a minha unidade do Ubuntu excluída.

Referência (com imagens): Como remover o Ubuntu de Inicialização dupla 
