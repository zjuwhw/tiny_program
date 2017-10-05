scr=../intersect.py
testfile1=test1.txt
testfile2=test2.txt
echo "================================"
echo "Test the script" $scr "..."
echo "==============================="

echo "1: python" $scr "--help"
echo "\n\n"
python $scr --help
echo "\n\n"

echo "2: python" $scr "--file1 test1.txt --file2 test2.txt"
echo "\n\n"
python $scr --file1 $testfile1 --file2 $testfile2
echo "\n\n"

echo "3: python" $scr "-f1 test1.txt -f2 test2.txt"
echo "\n\n"
python $scr -f1 $testfile1 -f2 $testfile2
echo "\n\n"

echo "4: python" $scr "-f1 test1.txt -f2 test2.txt -c1 1 -c2 2"
echo "\n\n"
python $scr -f1 $testfile1 -f2 $testfile2 -c1 1 -c2 2
echo "\n\n"
