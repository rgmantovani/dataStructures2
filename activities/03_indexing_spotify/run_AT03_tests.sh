echo "* Nome do programa:" "$1"
python3 $1  

echo "* Teste: poucos parametros de entrada - erro"
python3 $1  tests/query01.txt 

echo "* Teste: muitos parametros de entrada - erro"
python3 $1  spotify-1M.csv tests/query01.txt tests/op1.txt tmp1.txt output01.txt blz.txt 

echo "* Teste: arquivo de entrada inexistente - erro"
python3 $1 spotify-1M.csv ausente.txt output.txt

echo "* Teste: caso de teste 1"
python3 $1 spotify-1M.csv tests/query01.txt out01.txt
diff tests/output01.txt out01.txt > diferencas01.txt 

echo "* Teste: caso de teste 2"
python3 $1 spotify-1M.csv tests/query02.txt out02.txt 
diff tests/output02.txt out02.txt > diferencas02.txt 

echo "* Teste: caso de teste 3"
python3 $1 spotify-1M.csv tests/query03.txt out03.txt 
diff tests/output03.txt out03.txt > diferencas03.txt 

echo "* Teste: caso de teste 4 - arquivo errado - erro"
python3 $1 spotify-1M.csv tests/query04.txt out04.txt 
diff tests/output04.txt out04.txt > diferencas04.txt 

echo "* Teste: caso de teste 5 - arquivo vazio - erro"
python3 $1 spotify-1M.csv tests/query05.txt out05.txt 
diff tests/output05.txt out05.txt > diferencas05.txt 

echo "* Teste: caso de teste 6"
python3 $1 spotify-1M.csv tests/query06.txt out06.txt 
diff tests/output06.txt out06.txt > diferencas06.txt 

echo "* Teste: caso de teste 7"
python3 $1 spotify-1M.csv tests/query07.txt out07.txt 
diff tests/output07.txt out07.txt > diferencas07.txt 

echo "* Teste: caso de teste 8"
python3 $1 spotify-1M.csv tests/query08.txt out08.txt 
diff tests/output08.txt out08.txt > diferencas08.txt 

echo "* Teste: caso de teste 9"
python3 $1 spotify-1M.csv tests/query09.txt out09.txt 
diff tests/output09.txt out09.txt > diferencas09.txt 