# qa-code

Pastikan chromedriver sudah terinstall
Pastikan sudah membuat folder baru dan arahkan directori nya ke folder yang barusan dibuat.

1.	Install virtualenv 

“Virtualenv venv”pada terminal/cmd anda

2.	Nyalakan virtualenv 
“ . venv/bin/activate”

3.	Membuat folder requirement.txt
“Pip freeze > requirement.txt”

4.	Install semua requirement
“pip install  -r requirement.txt

5.	Running program
“behave feature/nama_file.feature”

6.	Generate Report
“behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features/nama_file.feature”

7.	Lihat Hasil report
“allure serve %allure_result_folder%”


TATA CARA 2

1.	Install virtualenv 

“Virtualenv venv”pada terminal/cmd anda

2.	Nyalakan virtualenv 
“ . venv/bin/activate”

3.	Install behave & loaddotenv
“pip install behave”
“pip install loaddotenv”

4.	Membuat folder requirement.txt
“Pip freeze > requirement.txt”

5.	Install semua requirement
“pip install  -r requirement.txt

6.	Running program
“behave feature/nama_file.feature”

7.	Generate Report
“behave -f allure_behave.formatter:AllureFormatter -o %allure_result_folder% ./features/nama_file.feature”

8.	Lihat Hasil report
“allure serve %allure_result_folder%”




