# -*- coding: utf-8 -*-
from django.db import models


class Document(models.Model):
	docfile = models.FileField(upload_to='documents/path')
    # docfile = models.FileField(upload_to='documents/%Y/%m/%d')
