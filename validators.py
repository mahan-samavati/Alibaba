from django.core.validators import RegexValidator

phone_number_validators = RegexValidator(
    regex=r'^09\d{9}$',
    message="شماره تلفن باید 11 رقم باشد و با 09 شروع شود"
)

national_code_validators = RegexValidator(
    regex=r'^\d{10}$',
    message="کد ملی درست وارد کنید"
)

persian_name_validators = RegexValidator(
    regex=r'^[ا-ی]+$',
    message="حروف باید فارسی و بدون عدد وارد شود"
)

english_name_validators = RegexValidator(
    regex=r'^[a-zA-Z]+$',
    message="حروف باید انگلیسی و بدون عدد وارد شود"
)