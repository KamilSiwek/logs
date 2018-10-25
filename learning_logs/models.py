"""Models file."""

from __future__ import unicode_literals

from django.db import models


class Topic(models.Model):
    """Users topic."""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Text type data."""
        return self.text


class Entry(models.Model):
    """Information about learn."""

    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Model's name when plural."""

        verbose_name_plural = 'entires'

    def __str__(self):
        """Return text format."""
        return self.text[:50] + "..."
