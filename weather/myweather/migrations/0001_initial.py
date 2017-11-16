# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('location', models.CharField(choices=[(b'Where Do you Live?', b'Where Do you Live?'), (b'New York,\tNew York', b'New York, New York'), (b'Los Angeles, California', b'Los Angeles, California'), (b'Chicago, Illinois', b'Chicago, Illinois'), (b'Houston, Texas', b'Houston, Texas'), (b'Philadelphia,\tPennsylvania', b'Philadelphia, Pennsylvania'), (b'Phoenix, Arizona', b'Phoenix, Arizona'), (b'San Antonio, Texas', b'San Antonio, Texas'), (b'San Diego, California', b'San Diego, California'), (b'Dallas, Texas', b'Dallas, Texas'), (b'San Jose,\tCalifornia', b'San Jose,\tCalifornia'), (b'Austin, Texas', b'Austin, Texas'), (b'Jacksonville,\tFlorida', b'Jacksonville, Florida'), (b'San Francisco, California', b'San Francisco, California'), (b'Indianapolis,\tIndiana', b'Indianapolis, Indiana'), (b'Columbus,\tOhio', b'Columbus, Ohio'), (b'Fort Worth, Texas', b'Fort Worth, Texas'), (b'Charlotte, North Carolina', b'Charlotte, North Carolina'), (b'Seattle, Washington', b'Seattle, Washington'), (b'Denver, Colorado', b'Denver, Colorado'), (b'El Paso, Texas', b'El Paso, Texas'), (b'Detroit, Michigan', b'Detroit,\tMichigan'), (b'Washington, District of Columbia', b'Washington, District of Columbia'), (b'Boston, Massachusetts', b'Boston, Massachusetts'), (b'Memphis, Tennessee', b'Memphis, Tennessee'), (b'Nashville, Tennessee', b'Nashville, Tennessee'), (b'Portland,\tOregon', b'Portland,\tOregon'), (b'Oklahoma City, Oklahoma', b'Oklahoma City,\tOklahoma'), (b'Las Vegas, Nevada', b'Las Vegas, Nevada'), (b'Baltimore, Maryland', b'Baltimore,\tMaryland'), (b'Louisville, Kentucky', b'Louisville, Kentucky'), (b'Milwaukee, Wisconsin', b'Milwaukee, Wisconsin'), (b'Albuquerque,\tNew Mexico', b'Albuquerque,\tNew Mexico'), (b'Tucson,\tArizona', b'Tucson,\tArizona'), (b'Fresno,\tCalifornia', b'Fresno,\tCalifornia'), (b'Sacramento,\tCalifornia', b'Sacramento,\tCalifornia'), (b'Kansas City,\tMissouri', b'Kansas City,\tMissouri'), (b'Long Beach,\tCalifornia', b'Long Beach,\tCalifornia'), (b'Mesa,\tArizona', b'Mesa,\tArizona'), (b'Atlanta,\tGeorgia', b'Atlanta,\tGeorgia'), (b'Colorado Springs,\tColorado', b'Colorado Springs,\tColorado'), (b'Virginia Beach,\tVirginia', b'Virginia Beach,\tVirginia'), (b'Raleigh, North Carolina', b'Raleigh, North Carolina'), (b'Omaha, Nebraska', b'Omaha,\tNebraska'), (b'Miami, Florida', b'Miami, Florida'), (b'Oakland, California', b'Oakland, California'), (b'Minneapolis, Minnesota', b'Minneapolis, Minnesota'), (b'Tulsa, Oklahoma', b'Tulsa,\tOklahoma'), (b'Wichita, Kansas', b'Wichita, Kansas'), (b'New Orleans, Louisiana', b'New Orleans, Louisiana'), (b'Arlington, Texas', b'Arlington, Texas'), (b'Cleveland, Ohio', b'Cleveland,\tOhio'), (b'Bakersfield, California', b'Bakersfield, California'), (b'Tampa, Florida', b'Tampa, Florida'), (b'Aurora, Colorado', b'Aurora, Colorado'), (b'Honolulu,\tHawai', b'Honolulu,\tHawai'), (b'Anaheim, California', b'Anaheim, California'), (b'Santa Ana, California', b'Santa Ana, California'), (b'Corpus Christi, Texas', b'Corpus Christi, Texas'), (b'Riverside, California', b'Riverside, California'), (b'St. Louis, Missouri', b'St. Louis,\tMissouri'), (b'Lexington, Kentucky', b'Lexington,\tKentucky'), (b'Stockton,\tCalifornia', b'Stockton,\tCalifornia'), (b'Pittsburgh, Pennsylvania', b'Pittsburgh, Pennsylvania'), (b'Saint Paul, Minnesota', b'Saint Paul, Minnesota'), (b'Anchorage, Alaska', b'Anchorage, Alaska'), (b'Cincinnati, Ohio', b'Cincinnati, Ohio'), (b'Henderson, Nevada', b'Henderson, Nevada'), (b'Greensboro, North Carolina', b'Greensboro,\tNorth Carolina'), (b'Plano, Texas', b'Plano, Texas'), (b'Newark, New Jersey', b'Newark,\tNew Jersey'), (b'Toledo, Ohio', b'Toledo, Ohio'), (b'Lincoln, Nebraska', b'Lincoln,\tNebraska'), (b'Orlando, Florida', b'Orlando, Florida'), (b'Chula Vista, California', b'Chula Vista, California'), (b'Jersey City, New Jersey', b'Jersey City, New Jersey'), (b'Chandler,\tArizona', b'Chandler, Arizona'), (b'Fort Wayne, Indiana', b'Fort Wayne, Indiana'), (b'Buffalo,\tNew York', b'Buffalo, New York'), (b'St. Petersburg, Florida', b'St. Petersburg, Florida'), (b'Irvine, California', b'Irvine,\tCalifornia'), (b'Laredo, Texas', b'Laredo, Texas'), (b'Lubbock, Texas', b'Lubbock, Texas'), (b'Madison, Wisconsin', b'Madison, Wisconsin'), (b'Gilbert, Arizona', b'Gilbert, Arizona'), (b'Norfolk, Virginia', b'Norfolk,\tVirginia'), (b'Reno, Nevada', b'Reno, Nevada'), (b'Winston\xe2\x80\x93Salem, North Carolina', b'Winston\xe2\x80\x93Salem, North Carolina'), (b'Glendale,\tArizona', b'Glendale, Arizona'), (b'Hialeah, Florida', b'Hialeah,\tFlorida'), (b'Garland, Texas', b'Garland, Texas'), (b'Scottsdale, Arizona', b'Scottsdale, Arizona'), (b'Irving, Texas', b'Irving, Texas'), (b'Chesapeake, Virginia', b'Chesapeake, Virginia'), (b'North Las Vegas,\tNevada', b'North Las Vegas, Nevada'), (b'Fremont, California', b'Fremont, California'), (b'Baton Rouge, Louisiana', b'Baton Rouge, Louisiana'), (b'Richmond,\tVirginia', b'Richmond, Virginia'), (b'Boise, Idaho', b'Boise, Idaho'), (b'San Bernardino,\tCalifornia', b'San Bernardino, California')], default='Where Do you live?', max_length=30)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weather',
            unique_together=set([('email', 'location')]),
        ),
    ]
