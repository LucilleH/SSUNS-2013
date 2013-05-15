import re

from mcmun.models import RegisteredSchool, ScholarshipApp

from django import forms


class EventForm(forms.ModelForm):
	class Meta:
		model = RegisteredSchool
		fields = (
			'num_pub_crawl',
			'num_non_alcohol',
		)


class RegistrationForm(forms.ModelForm):
	class Meta:
		model = RegisteredSchool
		fields = (
			'school_name',
			'first_time',
			'how_you_hear',
			'another_school',
			'other_method',
			'first_name',
			'last_name',
			'email',
			'delegate_email',
			'other_email',
			'address',
			'mail_address',
			'city',
			'province_state',
			'postal_code',
			'advisor_phone',
			'fax',
			'country',
			'country_1',
			'country_2',
			'country_3',
			'country_4',
			'country_5',
			'country_6',
			'country_7',
			'country_8',
			'country_9',
			'country_10',
			'committee_1',
			'committee_2',
			'committee_3',
			'committee_4',
			'experience',
			'mcgill_tours',
			'num_delegates',
			'use_online_payment',
			'disclaimer',

		)

	def clean_phone_number(self):
		phone_number = self.cleaned_data['phone_number']
		if re.search('[^0-9-+() ]+', phone_number) is not None:
			raise forms.ValidationError("")
		else:
			return phone_number


class ScholarshipForm(RegistrationForm):
	class Meta:
		model = ScholarshipApp
		exclude = ('school',)


class CommitteePrefsForm(forms.ModelForm):
	class Meta:
		model = RegisteredSchool
		fields = ('committee_1', 'committee_2', 'committee_3', 'committee_4', )
