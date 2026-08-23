==================== 25 XPath локаторів ====================

1) //header[@class='header bg-basic-dark']  — шапка сайту
2) //a[@class='header_logo']  — логотип
3) //a[text()='Home']  — пункт меню Home
4) //button[text()='About']  — кнопка About
5) //button[text()='Contacts']  — кнопка Contacts
6) //button[text()='Guest log in']  — кнопка Guest log in
7) //div[@class='header_right d-flex align-items-center']/button[contains(text(),'Sign In')]  — кнопка Sign In (складний)
8) //nav[@class='header_nav d-flex align-items-center']/button[@appscrollto='aboutSection']  — About у навігації (складний)
9) //h1[text()='Do more!']  — заголовок hero
10) //button[@class='hero-descriptor_btn btn btn-primary' and text()='Sign up']  — кнопка Sign up (text + @)
11) //section[@class='section hero']//iframe[@class='hero-video_frame']  — відео на головній (складний)
12) //div[@id='aboutSection']//p[text()='Log fuel expenses']  — заголовок блоку About (складний)
13) //div[@id='aboutSection']//p[text()='Instructions and manuals']  — другий блок About (складний)
14) //img[@alt='Instructions']  — зображення в блоці About
15) //div[@id='contactsSection']//h2[text()='Contacts']  — заголовок Contacts (складний)
16) //a[@href='https://ithillel.ua']  — посилання на сайт школи
17) //a[contains(@href,'mailto')]  — email-посилання
18) //div[@class='contacts_socials socials']//a[contains(@href,'facebook')]/span[contains(@class,'icon-facebook')]  — іконка Facebook (складний)
19) //footer//p[contains(text(),'Hillel IT school')]  — копірайт у футері (складний)
20) //h4[text()='Log in']  — заголовок модалки логіну
21) //input[@id='signinEmail']  — поле Email
22) //input[@formcontrolname='password']  — поле Password
23) //label[@for='signinEmail' and text()='Email']  — підпис поля Email (text + @)
24) //div[@class='modal-footer d-flex justify-content-between']/button[text()='Login']  — кнопка Login (складний)
25) //button[text()='Registration']  — кнопка Registration


==================== 25 CSS локаторів ====================

1) header.header.bg-basic-dark  — шапка сайту
2) a.header_logo  — логотип
3) nav.header_nav a.header-link[routerlink='/']  — пункт меню Home (складний + @)
4) button[appscrollto='aboutSection']  — кнопка About
5) button[appscrollto='contactsSection']  — кнопка Contacts
6) .header_right button.header-link.-guest  — кнопка Guest log in (складний)
7) .header_right button.btn-outline-white.header_signin  — кнопка Sign In (складний)
8) section.hero h1.hero-descriptor_title  — заголовок hero (складний)
9) p.hero-descriptor_descr.lead  — опис у hero
10) button.hero-descriptor_btn.btn.btn-primary  — кнопка Sign up
11) section.hero iframe.hero-video_frame  — відео на головній (складний)
12) #aboutSection  — секція About
13) #aboutSection .about-picture img[alt='Instructions']  — зображення в About (складний + @)
14) #aboutSection .about-block_title  — заголовки блоків About (складний)
15) #contactsSection h2  — заголовок Contacts (складний)
16) #contactsSection a.contacts_link[href='https://ithillel.ua']  — посилання на сайт (складний + @)
17) a.contacts_link[href^='mailto']  — email-посилання (@ починається з)
18) .contacts_socials a[href*='facebook'] span.icon-facebook  — іконка Facebook (складний + @)
19) .form-check input#remember[type='checkbox']  — чекбокс Remember me (складний + @)
20) footer.footer .footer_item p  — текст у футері (складний)
21) footer a.footer_logo  — логотип у футері (складний)
22) .modal-content .modal-header h4.modal-title  — заголовок модалки (складний)
23) .modal-body input#signinEmail  — поле Email (складний)
24) input[formcontrolname='password']  — поле Password (@)
25) .modal-footer button.btn-primary  — кнопка Login (складний)
