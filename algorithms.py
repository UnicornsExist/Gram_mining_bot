# This script contains all algorithms I use in bot

def referral_link_check(user_id, link):
	# (ВАЖНО!)
	# Здесь я должен проверить человека, нажавшего на /start на
	# его наличие в базе данных бота для того, чтобы один человек
	# не мог дважды стать чьим-то рефералом

	if len(link.split(' ')) == 2:    # Если линка выглядит следующим образом : /start 12345, где 12345 - ID пригласившего человека
		





