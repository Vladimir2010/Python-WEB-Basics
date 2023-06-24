from django.contrib import admin

# Register your models here.


class Comment(models.Model):
    comment_text = models.Text_Field(max_length=300, blank=False, null=False)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
