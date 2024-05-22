echo "* Nome do programa:" "$1"
python3 $1  

echo "* Teste: poucos parametros de entrada"
python3 $1  tests/input1.txt 

echo "* Teste: muitos parametros de entrada"
python3 $1  tests/input1.txt tests/op1.txt tmp1.txt output1.txt blz.txt 

echo "* Teste: arquivo de entrada inexistente"
python3 $1 ausente.txt output.txt

echo "* Teste: caso de teste 1"
python3 $1 tests/input1.txt output1.txt 

echo "* Teste: caso de teste 2"
python3 $1 tests/input2.txt output2.txt 

echo "* Teste: caso de teste 3"
python3 $1 tests/input3.txt output3.txt 

echo "* Teste: caso de teste 4"
python3 $1 tests/input4.txt output4.txt 

echo "* Teste: caso de teste 5"
python3 $1 tests/input5.txt output5.txt 

echo "* Teste: caso de teste 6"
python3 $1 tests/input6.txt output6.txt 

echo "* Teste: caso de teste 7"
python3 $1 tests/input7.txt output7.txt 

echo "* Teste: caso de teste 8 - arquivo vazio - erro"
python3 $1 tests/input8.txt output8.txt 

echo "* Teste: caso de teste 9 - arquivo inválido"
python3 $1 tests/input9.txt output9.txt 
