echo "* Nome do programa:" "$1"
python3 $1  

echo "* Teste: poucos parametros de entrada"
python3 $1  tests/input01.txt 

echo "* Teste: muitos parametros de entrada"
python3 $1  tests/input01.txt tests/op1.txt tmp1.txt output01.txt blz.txt 

echo "* Teste: arquivo de entrada inexistente"
python3 $1 ausente.txt output.txt

echo "* Teste: caso de teste 1"
python3 $1 tests/input01.txt output01.txt
diff tests/output01.txt output01.txt > diferencas01.txt 

echo "* Teste: caso de teste 2"
python3 $1 tests/input02.txt output02.txt 
diff tests/output02.txt output02.txt > diferencas02.txt 

echo "* Teste: caso de teste 3"
python3 $1 tests/input03.txt output03.txt 
diff tests/output03.txt output03.txt > diferencas03.txt 

echo "* Teste: caso de teste 4"
python3 $1 tests/input04.txt output04.txt 
diff tests/output04.txt output04.txt > diferencas04.txt 

echo "* Teste: caso de teste 5"
python3 $1 tests/input05.txt output05.txt 
diff tests/output05.txt output05.txt > diferencas05.txt 

echo "* Teste: caso de teste 6"
python3 $1 tests/input06.txt output06.txt 
diff tests/output06.txt output06.txt > diferencas06.txt 

echo "* Teste: caso de teste 7 - arquivo vazio - erro"
python3 $1 tests/input07.txt output07.txt 

echo "* Teste: caso de teste 8 - arquivo inválido"
python3 $1 tests/input08.txt output08.txt 