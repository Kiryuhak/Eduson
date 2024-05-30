import requests
import allure
from random import randrange

from config import url
from checkers.checkers import check_not_empty, check_status_200, check_status_201, check_status_404, check_schema
#from data.validate import validate_json
from steps.vote import Vote


@allure.suite("thecatapi")
@allure.title("Test random vote")
def test_get_votes(headers: dict) -> None:
	vote = Vote(headers)

	# get all votes
	votes = vote.get_votes()

	# choose random vote id
	i = randrange(len(votes))
	check_schema('votes', votes[i])
	id = votes[i]['id']

	# get random vote by id and check it
	vote.get_vote(id)


@allure.suite("thecatapi")
@allure.title("Test creation and deletion of the vote")
def test_create_vote(headers) -> None:
	vote = Vote(headers)

	# create vote
	id = vote.create_vote()

	# get this vote and check it
	vote.get_vote(id)

	# delete vote
	vote.delete_vote(id)

	# trying to get deleted vote
	vote.get_deleted_vote(id)


