from django.db import models

STATE_CHOICE=(
    ("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),
    ("Andhra Pradesh","Andhra Pradesh"),
    ("Arunachal Pradesh ","Arunachal Pradesh "),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Chandigarh","Chandigarh"),
    ("Chhattisgarh","Chhattisgarh"),
    ("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),
    ("Daman and Diu","Daman and Diu"),
    ("Delhi","Delhi"),
    ("Goa","Goa"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("Himachal Pradesh","Himachal Pradesh"),
    ("Jammu and Kashmir ","Jammu and Kashmir "),
    ("Jharkhand","Jharkhand"),
    ("Karnataka","Karnataka"),
    ("Kerala","Kerala"),
    ("Lakshadweep","Lakshadweep"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Maharashtra","Maharashtra"),
    ("Manipur","Manipur"),
    ("Meghalaya","Meghalaya"),
    ("Mizoram","Mizoram"),
    ("Nagaland","Nagaland"),
    ("Odisha","Odisha"),
    ("Puducherry","Puducherry"),
    ("Punjab","Punjab"),
    ("Rajasthan","Rajasthan"),
    ("Sikkim","Sikkim"),
    ("Tamil Nadu","Tamil Nadu"),
    ("Telangana","Telangana"),
    ("Tripura","Tripura"),
    ("Uttar Pradesh","Uttar Pradesh"),
    ("Uttarakhand","Uttarakhand"),
    ("West Bengal","West Bengal"),

)

JOB_ROLE_CHOICE=(
    ('Account Executive','Account Executive'),
    ('Account Manager','Account Manager'),
    ('Accountant','Accountant'),
    ('Business Analyst','Business Analyst'),
    ('Customer Service Representative','Customer Service Representative'),
    ('Engineer','Engineer'),
    ('Human Resoure','Human Resoure'),
    ('Hiring Manager','Hiring Manager'),
    ('Information Security','Information Security'),
    ('Marketing','Marketing'),
    ('Marketing Manager','Marketing Manager'),
    ('Project Manager','Project Manager'),
    ('Sales','Sales'),
    ('Software Engineer','Software Engineer'),
    ('Web Developer','Web Developer'),
    ('Others','Others'),
)

class resume(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    dob=models.DateField(auto_now=False,auto_now_add=False) #will not automatically add date
    gender=models.CharField(max_length=20)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pin=models.PositiveIntegerField()
    state=models.CharField(choices=STATE_CHOICE,max_length=70)
    mobile=models.PositiveIntegerField()
    jobtype=models.CharField(choices=JOB_ROLE_CHOICE,max_length=70)
    jobcity=models.CharField(max_length=50)
    profile_image=models.ImageField(upload_to='profileimage',blank=True) #blank=True if somebody doesnt give image then it will also work
    doc=models.FileField(upload_to='doc',blank=True)