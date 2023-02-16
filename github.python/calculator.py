                    #ماشين حساب
def cal():
    moj1 = int(input('عدد اول خود را وارد کنيد: '))
    moj2 = int(input('عدد دوم خود را وارد کنيد: '))
    moj3 = input('عملگر خود را وارد کنيد ')
    if   moj3  == '+'  :
        # جمع
        print('{} + {} = '.format(moj1, moj2))
        print(moj1 + moj2)
    elif moj3  == '-'  :
        # تفريق
        print('{} - {} = '.format(moj1, moj2))
        print(moj1 - moj2)
    elif moj3 == '*' :
        # ضرب
        print('{} * {} = '.format(moj1, moj2))
        print(moj1 * moj2)
    elif moj3 == '/' :
        # تقسيم
        print('{} / {} = '.format(moj1, moj2))
        print(moj1 / moj2)
cal()
tekrar = str(input('bra adame Y,y type konid'))
if tekrar == "Y" or tekrar == 'y' :
   print(cal())
else:
   print('goodbye')
