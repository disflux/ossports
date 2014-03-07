# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Addresses(models.Model):
    id = models.IntegerField(primary_key=True)
    location = models.ForeignKey('Locations')
    language = models.CharField(max_length=100, blank=True)
    suite = models.CharField(max_length=100, blank=True)
    floor = models.CharField(max_length=100, blank=True)
    building = models.CharField(max_length=100, blank=True)
    street_number = models.CharField(max_length=100, blank=True)
    street_prefix = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    street_suffix = models.CharField(max_length=100, blank=True)
    neighborhood = models.CharField(max_length=100, blank=True)
    district = models.CharField(max_length=100, blank=True)
    locality = models.CharField(max_length=100, blank=True)
    county = models.CharField(max_length=100, blank=True)
    region = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'addresses'

class AffiliationPhases(models.Model):
    id = models.IntegerField(primary_key=True)
    affiliation = models.ForeignKey('Affiliations')
    root_id = models.IntegerField(blank=True, null=True)
    ancestor_affiliation = models.ForeignKey('Affiliations', blank=True, null=True)
    start_season = models.ForeignKey('Seasons', blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_season = models.ForeignKey('Seasons', blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'affiliation_phases'

class Affiliations(models.Model):
    id = models.IntegerField(primary_key=True)
    affiliation_key = models.CharField(max_length=100)
    affiliation_type = models.CharField(max_length=100, blank=True)
    publisher = models.ForeignKey('Publishers')
    class Meta:
        managed = False
        db_table = 'affiliations'

class AffiliationsDocuments(models.Model):
    affiliation = models.ForeignKey(Affiliations)
    document = models.ForeignKey('Documents')
    class Meta:
        managed = False
        db_table = 'affiliations_documents'

class AffiliationsEvents(models.Model):
    affiliation = models.ForeignKey(Affiliations)
    event = models.ForeignKey('Events')
    class Meta:
        managed = False
        db_table = 'affiliations_events'

class AffiliationsMedia(models.Model):
    affiliation = models.ForeignKey(Affiliations)
    media = models.ForeignKey('Media')
    class Meta:
        managed = False
        db_table = 'affiliations_media'

class AmericanFootballActionParticipants(models.Model):
    id = models.IntegerField(primary_key=True)
    american_football_action_play = models.ForeignKey('AmericanFootballActionPlays')
    person = models.ForeignKey('Persons')
    participant_role = models.CharField(max_length=100)
    score_type = models.CharField(max_length=100, blank=True)
    field_line = models.IntegerField(blank=True, null=True)
    yardage = models.IntegerField(blank=True, null=True)
    score_credit = models.IntegerField(blank=True, null=True)
    yards_gained = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_action_participants'

class AmericanFootballActionPlays(models.Model):
    id = models.IntegerField(primary_key=True)
    american_football_event_state = models.ForeignKey('AmericanFootballEventStates')
    team = models.ForeignKey('Teams', blank=True, null=True)
    play_type = models.CharField(max_length=100, blank=True)
    score_attempt_type = models.CharField(max_length=100, blank=True)
    touchdown_type = models.CharField(max_length=100, blank=True)
    drive_result = models.CharField(max_length=100, blank=True)
    points = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_action_plays'

class AmericanFootballDefensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    tackles_total = models.CharField(max_length=100, blank=True)
    tackles_solo = models.CharField(max_length=100, blank=True)
    tackles_assists = models.CharField(max_length=100, blank=True)
    interceptions_total = models.CharField(max_length=100, blank=True)
    interceptions_yards = models.CharField(max_length=100, blank=True)
    interceptions_average = models.CharField(max_length=100, blank=True)
    interceptions_longest = models.CharField(max_length=100, blank=True)
    interceptions_touchdown = models.CharField(max_length=100, blank=True)
    quarterback_hurries = models.CharField(max_length=100, blank=True)
    sacks_total = models.CharField(max_length=100, blank=True)
    sacks_yards = models.CharField(max_length=100, blank=True)
    passes_defensed = models.CharField(max_length=100, blank=True)
    first_downs_against_total = models.IntegerField(blank=True, null=True)
    first_downs_against_rushing = models.IntegerField(blank=True, null=True)
    first_downs_against_passing = models.IntegerField(blank=True, null=True)
    first_downs_against_penalty = models.IntegerField(blank=True, null=True)
    conversions_third_down_against = models.IntegerField(blank=True, null=True)
    conversions_third_down_against_attempts = models.IntegerField(blank=True, null=True)
    conversions_third_down_against_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    conversions_fourth_down_against = models.IntegerField(blank=True, null=True)
    conversions_fourth_down_against_attempts = models.IntegerField(blank=True, null=True)
    conversions_fourth_down_against_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    two_point_conversions_against = models.IntegerField(blank=True, null=True)
    two_point_conversions_against_attempts = models.IntegerField(blank=True, null=True)
    offensive_plays_against_touchdown = models.IntegerField(blank=True, null=True)
    offensive_plays_against_average_yards_per_game = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rushes_against_attempts = models.IntegerField(blank=True, null=True)
    rushes_against_yards = models.IntegerField(blank=True, null=True)
    rushing_against_average_yards_per_game = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rushes_against_touchdowns = models.IntegerField(blank=True, null=True)
    rushes_against_average_yards_per = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    rushes_against_longest = models.IntegerField(blank=True, null=True)
    receptions_against_total = models.IntegerField(blank=True, null=True)
    receptions_against_yards = models.IntegerField(blank=True, null=True)
    receptions_against_touchdowns = models.IntegerField(blank=True, null=True)
    receptions_against_average_yards_per = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    receptions_against_longest = models.IntegerField(blank=True, null=True)
    passes_against_yards_net = models.IntegerField(blank=True, null=True)
    passes_against_yards_gross = models.IntegerField(blank=True, null=True)
    passes_against_attempts = models.IntegerField(blank=True, null=True)
    passes_against_completions = models.IntegerField(blank=True, null=True)
    passes_against_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passes_against_average_yards_per_game = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passes_against_average_yards_per = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passes_against_touchdowns = models.IntegerField(blank=True, null=True)
    passes_against_touchdowns_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    passes_against_longest = models.IntegerField(blank=True, null=True)
    passes_against_rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    interceptions_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_defensive_stats'

class AmericanFootballDownProgressStats(models.Model):
    id = models.IntegerField(primary_key=True)
    first_downs_total = models.CharField(max_length=100, blank=True)
    first_downs_pass = models.CharField(max_length=100, blank=True)
    first_downs_run = models.CharField(max_length=100, blank=True)
    first_downs_penalty = models.CharField(max_length=100, blank=True)
    conversions_third_down = models.CharField(max_length=100, blank=True)
    conversions_third_down_attempts = models.CharField(max_length=100, blank=True)
    conversions_third_down_percentage = models.CharField(max_length=100, blank=True)
    conversions_fourth_down = models.CharField(max_length=100, blank=True)
    conversions_fourth_down_attempts = models.CharField(max_length=100, blank=True)
    conversions_fourth_down_percentage = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_down_progress_stats'

class AmericanFootballEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey('Events')
    current_state = models.SmallIntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    period_value = models.IntegerField(blank=True, null=True)
    period_time_elapsed = models.CharField(max_length=100, blank=True)
    period_time_remaining = models.CharField(max_length=100, blank=True)
    clock_state = models.CharField(max_length=100, blank=True)
    down = models.IntegerField(blank=True, null=True)
    team_in_possession = models.ForeignKey('Teams', blank=True, null=True)
    score_team = models.IntegerField(blank=True, null=True)
    score_team_opposing = models.IntegerField(blank=True, null=True)
    distance_for_1st_down = models.IntegerField(blank=True, null=True)
    field_side = models.CharField(max_length=100, blank=True)
    field_line = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=40, blank=True)
    score_team_away = models.IntegerField(blank=True, null=True)
    score_team_home = models.IntegerField(blank=True, null=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_event_states'

class AmericanFootballFumblesStats(models.Model):
    id = models.IntegerField(primary_key=True)
    fumbles_committed = models.CharField(max_length=100, blank=True)
    fumbles_forced = models.CharField(max_length=100, blank=True)
    fumbles_recovered = models.CharField(max_length=100, blank=True)
    fumbles_lost = models.CharField(max_length=100, blank=True)
    fumbles_yards_gained = models.CharField(max_length=100, blank=True)
    fumbles_own_committed = models.CharField(max_length=100, blank=True)
    fumbles_own_recovered = models.CharField(max_length=100, blank=True)
    fumbles_own_lost = models.CharField(max_length=100, blank=True)
    fumbles_own_yards_gained = models.CharField(max_length=100, blank=True)
    fumbles_opposing_committed = models.CharField(max_length=100, blank=True)
    fumbles_opposing_recovered = models.CharField(max_length=100, blank=True)
    fumbles_opposing_lost = models.CharField(max_length=100, blank=True)
    fumbles_opposing_yards_gained = models.CharField(max_length=100, blank=True)
    fumbles_own_touchdowns = models.IntegerField(blank=True, null=True)
    fumbles_opposing_touchdowns = models.IntegerField(blank=True, null=True)
    fumbles_committed_defense = models.IntegerField(blank=True, null=True)
    fumbles_committed_special_teams = models.IntegerField(blank=True, null=True)
    fumbles_committed_other = models.IntegerField(blank=True, null=True)
    fumbles_lost_defense = models.IntegerField(blank=True, null=True)
    fumbles_lost_special_teams = models.IntegerField(blank=True, null=True)
    fumbles_lost_other = models.IntegerField(blank=True, null=True)
    fumbles_forced_defense = models.IntegerField(blank=True, null=True)
    fumbles_recovered_defense = models.IntegerField(blank=True, null=True)
    fumbles_recovered_special_teams = models.IntegerField(blank=True, null=True)
    fumbles_recovered_other = models.IntegerField(blank=True, null=True)
    fumbles_recovered_yards_defense = models.IntegerField(blank=True, null=True)
    fumbles_recovered_yards_special_teams = models.IntegerField(blank=True, null=True)
    fumbles_recovered_yards_other = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_fumbles_stats'

class AmericanFootballOffensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    offensive_plays_yards = models.CharField(max_length=100, blank=True)
    offensive_plays_number = models.CharField(max_length=100, blank=True)
    offensive_plays_average_yards_per = models.CharField(max_length=100, blank=True)
    possession_duration = models.CharField(max_length=100, blank=True)
    turnovers_giveaway = models.CharField(max_length=100, blank=True)
    tackles = models.IntegerField(blank=True, null=True)
    tackles_assists = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_offensive_stats'

class AmericanFootballPassingStats(models.Model):
    id = models.IntegerField(primary_key=True)
    passes_attempts = models.CharField(max_length=100, blank=True)
    passes_completions = models.CharField(max_length=100, blank=True)
    passes_percentage = models.CharField(max_length=100, blank=True)
    passes_yards_gross = models.CharField(max_length=100, blank=True)
    passes_yards_net = models.CharField(max_length=100, blank=True)
    passes_yards_lost = models.CharField(max_length=100, blank=True)
    passes_touchdowns = models.CharField(max_length=100, blank=True)
    passes_touchdowns_percentage = models.CharField(max_length=100, blank=True)
    passes_interceptions = models.CharField(max_length=100, blank=True)
    passes_interceptions_percentage = models.CharField(max_length=100, blank=True)
    passes_longest = models.CharField(max_length=100, blank=True)
    passes_average_yards_per = models.CharField(max_length=100, blank=True)
    passer_rating = models.CharField(max_length=100, blank=True)
    receptions_total = models.CharField(max_length=100, blank=True)
    receptions_yards = models.CharField(max_length=100, blank=True)
    receptions_touchdowns = models.CharField(max_length=100, blank=True)
    receptions_first_down = models.CharField(max_length=100, blank=True)
    receptions_longest = models.CharField(max_length=100, blank=True)
    receptions_average_yards_per = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_passing_stats'

class AmericanFootballPenaltiesStats(models.Model):
    id = models.IntegerField(primary_key=True)
    penalties_total = models.CharField(max_length=100, blank=True)
    penalty_yards = models.CharField(max_length=100, blank=True)
    penalty_first_downs = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_penalties_stats'

class AmericanFootballRushingStats(models.Model):
    id = models.IntegerField(primary_key=True)
    rushes_attempts = models.CharField(max_length=100, blank=True)
    rushes_yards = models.CharField(max_length=100, blank=True)
    rushes_touchdowns = models.CharField(max_length=100, blank=True)
    rushing_average_yards_per = models.CharField(max_length=100, blank=True)
    rushes_first_down = models.CharField(max_length=100, blank=True)
    rushes_longest = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_rushing_stats'

class AmericanFootballSacksAgainstStats(models.Model):
    id = models.IntegerField(primary_key=True)
    sacks_against_yards = models.CharField(max_length=100, blank=True)
    sacks_against_total = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_sacks_against_stats'

class AmericanFootballScoringStats(models.Model):
    id = models.IntegerField(primary_key=True)
    touchdowns_total = models.CharField(max_length=100, blank=True)
    touchdowns_passing = models.CharField(max_length=100, blank=True)
    touchdowns_rushing = models.CharField(max_length=100, blank=True)
    touchdowns_special_teams = models.CharField(max_length=100, blank=True)
    touchdowns_defensive = models.CharField(max_length=100, blank=True)
    extra_points_attempts = models.CharField(max_length=100, blank=True)
    extra_points_made = models.CharField(max_length=100, blank=True)
    extra_points_missed = models.CharField(max_length=100, blank=True)
    extra_points_blocked = models.CharField(max_length=100, blank=True)
    field_goal_attempts = models.CharField(max_length=100, blank=True)
    field_goals_made = models.CharField(max_length=100, blank=True)
    field_goals_missed = models.CharField(max_length=100, blank=True)
    field_goals_blocked = models.CharField(max_length=100, blank=True)
    safeties_against = models.CharField(max_length=100, blank=True)
    two_point_conversions_attempts = models.CharField(max_length=100, blank=True)
    two_point_conversions_made = models.CharField(max_length=100, blank=True)
    touchbacks_total = models.CharField(max_length=100, blank=True)
    safeties_against_opponent = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_scoring_stats'

class AmericanFootballSpecialTeamsStats(models.Model):
    id = models.IntegerField(primary_key=True)
    returns_punt_total = models.CharField(max_length=100, blank=True)
    returns_punt_yards = models.CharField(max_length=100, blank=True)
    returns_punt_average = models.CharField(max_length=100, blank=True)
    returns_punt_longest = models.CharField(max_length=100, blank=True)
    returns_punt_touchdown = models.CharField(max_length=100, blank=True)
    returns_kickoff_total = models.CharField(max_length=100, blank=True)
    returns_kickoff_yards = models.CharField(max_length=100, blank=True)
    returns_kickoff_average = models.CharField(max_length=100, blank=True)
    returns_kickoff_longest = models.CharField(max_length=100, blank=True)
    returns_kickoff_touchdown = models.CharField(max_length=100, blank=True)
    returns_total = models.CharField(max_length=100, blank=True)
    returns_yards = models.CharField(max_length=100, blank=True)
    punts_total = models.CharField(max_length=100, blank=True)
    punts_yards_gross = models.CharField(max_length=100, blank=True)
    punts_yards_net = models.CharField(max_length=100, blank=True)
    punts_longest = models.CharField(max_length=100, blank=True)
    punts_inside_20 = models.CharField(max_length=100, blank=True)
    punts_inside_20_percentage = models.CharField(max_length=100, blank=True)
    punts_average = models.CharField(max_length=100, blank=True)
    punts_blocked = models.CharField(max_length=100, blank=True)
    touchbacks_total = models.CharField(max_length=100, blank=True)
    touchbacks_total_percentage = models.CharField(max_length=100, blank=True)
    touchbacks_kickoffs = models.CharField(max_length=100, blank=True)
    touchbacks_kickoffs_percentage = models.CharField(max_length=100, blank=True)
    touchbacks_punts = models.CharField(max_length=100, blank=True)
    touchbacks_punts_percentage = models.CharField(max_length=100, blank=True)
    touchbacks_interceptions = models.CharField(max_length=100, blank=True)
    touchbacks_interceptions_percentage = models.CharField(max_length=100, blank=True)
    fair_catches = models.CharField(max_length=100, blank=True)
    punts_against_blocked = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts_1_to_19 = models.IntegerField(blank=True, null=True)
    field_goals_against_made_1_to_19 = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts_20_to_29 = models.IntegerField(blank=True, null=True)
    field_goals_against_made_20_to_29 = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts_30_to_39 = models.IntegerField(blank=True, null=True)
    field_goals_against_made_30_to_39 = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts_40_to_49 = models.IntegerField(blank=True, null=True)
    field_goals_against_made_40_to_49 = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts_50_plus = models.IntegerField(blank=True, null=True)
    field_goals_against_made_50_plus = models.IntegerField(blank=True, null=True)
    field_goals_against_attempts = models.IntegerField(blank=True, null=True)
    extra_points_against_attempts = models.IntegerField(blank=True, null=True)
    tackles = models.IntegerField(blank=True, null=True)
    tackles_assists = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'american_football_special_teams_stats'

class AmericanFootballTeamStats(models.Model):
    id = models.IntegerField(primary_key=True)
    yards_per_attempt = models.CharField(max_length=100, blank=True)
    average_starting_position = models.CharField(max_length=100, blank=True)
    timeouts = models.CharField(max_length=100, blank=True)
    time_of_possession = models.CharField(max_length=100, blank=True)
    turnover_ratio = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'american_football_team_stats'

class Awards(models.Model):
    id = models.IntegerField(primary_key=True)
    participant_type = models.CharField(max_length=100)
    participant_id = models.IntegerField()
    award_type = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, blank=True)
    total = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True)
    award_value = models.CharField(max_length=100, blank=True)
    currency = models.CharField(max_length=100, blank=True)
    date_coverage_type = models.CharField(max_length=100, blank=True)
    date_coverage_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'awards'

class BaseballActionContactDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    baseball_action_pitch = models.ForeignKey('BaseballActionPitches')
    location = models.CharField(max_length=100, blank=True)
    strength = models.CharField(max_length=100, blank=True)
    velocity = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    trajectory_coordinates = models.CharField(max_length=100, blank=True)
    trajectory_formula = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'baseball_action_contact_details'

class BaseballActionPitches(models.Model):
    id = models.IntegerField(primary_key=True)
    baseball_action_play = models.ForeignKey('BaseballActionPlays')
    sequence_number = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    baseball_defensive_group = models.ForeignKey('BaseballDefensiveGroup', blank=True, null=True)
    umpire_call = models.CharField(max_length=100, blank=True)
    pitch_location = models.CharField(max_length=100, blank=True)
    pitch_type = models.CharField(max_length=100, blank=True)
    pitch_velocity = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=2048, blank=True)
    trajectory_coordinates = models.CharField(max_length=512, blank=True)
    trajectory_formula = models.CharField(max_length=100, blank=True)
    ball_type = models.CharField(max_length=40, blank=True)
    strike_type = models.CharField(max_length=40, blank=True)
    strikes = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseball_action_pitches'

class BaseballActionPlays(models.Model):
    id = models.IntegerField(primary_key=True)
    baseball_event_state = models.ForeignKey('BaseballEventStates')
    play_type = models.CharField(max_length=100, blank=True)
    out_type = models.CharField(max_length=100, blank=True)
    notation = models.CharField(max_length=100, blank=True)
    notation_yaml = models.TextField(blank=True)
    baseball_defensive_group_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    runner_on_first_advance = models.CharField(max_length=40, blank=True)
    runner_on_second_advance = models.CharField(max_length=40, blank=True)
    runner_on_third_advance = models.CharField(max_length=40, blank=True)
    outs_recorded = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    runs_scored = models.IntegerField(blank=True, null=True)
    earned_runs_scored = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'baseball_action_plays'

class BaseballActionSubstitutions(models.Model):
    id = models.IntegerField(primary_key=True)
    baseball_event_state = models.ForeignKey('BaseballEventStates')
    sequence_number = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    person_type = models.CharField(max_length=100, blank=True)
    person_original = models.ForeignKey('Persons', blank=True, null=True)
    person_original_position = models.ForeignKey('Positions', blank=True, null=True)
    person_original_lineup_slot = models.IntegerField(blank=True, null=True)
    person_replacing = models.ForeignKey('Persons', blank=True, null=True)
    person_replacing_position = models.ForeignKey('Positions', blank=True, null=True)
    person_replacing_lineup_slot = models.IntegerField(blank=True, null=True)
    substitution_reason = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'baseball_action_substitutions'

class BaseballDefensiveGroup(models.Model):
    id = models.IntegerField(primary_key=True)
    class Meta:
        managed = False
        db_table = 'baseball_defensive_group'

class BaseballDefensivePlayers(models.Model):
    id = models.IntegerField(primary_key=True)
    baseball_defensive_group = models.ForeignKey(BaseballDefensiveGroup)
    player = models.ForeignKey('Persons')
    position = models.ForeignKey('Positions')
    class Meta:
        managed = False
        db_table = 'baseball_defensive_players'

class BaseballDefensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    double_plays = models.IntegerField(blank=True, null=True)
    triple_plays = models.IntegerField(blank=True, null=True)
    putouts = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    errors = models.IntegerField(blank=True, null=True)
    fielding_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    defensive_average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    errors_passed_ball = models.IntegerField(blank=True, null=True)
    errors_catchers_interference = models.IntegerField(blank=True, null=True)
    stolen_bases_average = models.IntegerField(blank=True, null=True)
    stolen_bases_caught = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseball_defensive_stats'

class BaseballEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey('Events')
    current_state = models.SmallIntegerField(blank=True, null=True)
    sequence_number = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)
    at_bat_number = models.IntegerField(blank=True, null=True)
    inning_value = models.IntegerField(blank=True, null=True)
    inning_half = models.CharField(max_length=100, blank=True)
    outs = models.IntegerField(blank=True, null=True)
    balls = models.IntegerField(blank=True, null=True)
    strikes = models.IntegerField(blank=True, null=True)
    runner_on_first = models.ForeignKey('Persons', blank=True, null=True)
    runner_on_second = models.ForeignKey('Persons', blank=True, null=True)
    runner_on_third = models.ForeignKey('Persons', blank=True, null=True)
    runner_on_first_0 = models.SmallIntegerField(db_column='runner_on_first', blank=True, null=True) # Field renamed because of name conflict.
    runner_on_second_0 = models.SmallIntegerField(db_column='runner_on_second', blank=True, null=True) # Field renamed because of name conflict.
    runner_on_third_0 = models.SmallIntegerField(db_column='runner_on_third', blank=True, null=True) # Field renamed because of name conflict.
    runs_this_inning_half = models.IntegerField(blank=True, null=True)
    pitcher = models.ForeignKey('Persons', blank=True, null=True)
    batter = models.ForeignKey('Persons', blank=True, null=True)
    batter_side = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseball_event_states'

class BaseballOffensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    runs_scored = models.IntegerField(blank=True, null=True)
    at_bats = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    rbi = models.IntegerField(blank=True, null=True)
    total_bases = models.IntegerField(blank=True, null=True)
    slugging_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    bases_on_balls = models.IntegerField(blank=True, null=True)
    strikeouts = models.IntegerField(blank=True, null=True)
    left_on_base = models.IntegerField(blank=True, null=True)
    left_in_scoring_position = models.IntegerField(blank=True, null=True)
    singles = models.IntegerField(blank=True, null=True)
    doubles = models.IntegerField(blank=True, null=True)
    triples = models.IntegerField(blank=True, null=True)
    home_runs = models.IntegerField(blank=True, null=True)
    grand_slams = models.IntegerField(blank=True, null=True)
    at_bats_per_rbi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plate_appearances_per_rbi = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    at_bats_per_home_run = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plate_appearances_per_home_run = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sac_flies = models.IntegerField(blank=True, null=True)
    sac_bunts = models.IntegerField(blank=True, null=True)
    grounded_into_double_play = models.IntegerField(blank=True, null=True)
    moved_up = models.IntegerField(blank=True, null=True)
    on_base_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    stolen_bases = models.IntegerField(blank=True, null=True)
    stolen_bases_caught = models.IntegerField(blank=True, null=True)
    stolen_bases_average = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    hit_by_pitch = models.IntegerField(blank=True, null=True)
    on_base_plus_slugging = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    plate_appearances = models.IntegerField(blank=True, null=True)
    hits_extra_base = models.IntegerField(blank=True, null=True)
    pick_offs_against = models.IntegerField(blank=True, null=True)
    sacrifices = models.IntegerField(blank=True, null=True)
    outs_fly = models.IntegerField(blank=True, null=True)
    outs_ground = models.IntegerField(blank=True, null=True)
    reached_base_defensive_interference = models.IntegerField(blank=True, null=True)
    reached_base_error = models.IntegerField(blank=True, null=True)
    reached_base_fielder_choice = models.IntegerField(blank=True, null=True)
    double_plays_against = models.IntegerField(blank=True, null=True)
    triple_plays_against = models.IntegerField(blank=True, null=True)
    strikeouts_looking = models.IntegerField(blank=True, null=True)
    bases_on_balls_intentional = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseball_offensive_stats'

class BaseballPitchingStats(models.Model):
    id = models.IntegerField(primary_key=True)
    runs_allowed = models.IntegerField(blank=True, null=True)
    singles_allowed = models.IntegerField(blank=True, null=True)
    doubles_allowed = models.IntegerField(blank=True, null=True)
    triples_allowed = models.IntegerField(blank=True, null=True)
    home_runs_allowed = models.IntegerField(blank=True, null=True)
    innings_pitched = models.CharField(max_length=20, blank=True)
    hits = models.IntegerField(blank=True, null=True)
    earned_runs = models.IntegerField(blank=True, null=True)
    unearned_runs = models.IntegerField(blank=True, null=True)
    bases_on_balls = models.IntegerField(blank=True, null=True)
    bases_on_balls_intentional = models.IntegerField(blank=True, null=True)
    strikeouts = models.IntegerField(blank=True, null=True)
    strikeout_to_bb_ratio = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    number_of_pitches = models.IntegerField(blank=True, null=True)
    era = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inherited_runners_scored = models.IntegerField(blank=True, null=True)
    pick_offs = models.IntegerField(blank=True, null=True)
    errors_hit_with_pitch = models.IntegerField(blank=True, null=True)
    errors_wild_pitch = models.IntegerField(blank=True, null=True)
    balks = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    shutouts = models.IntegerField(blank=True, null=True)
    games_complete = models.IntegerField(blank=True, null=True)
    games_finished = models.IntegerField(blank=True, null=True)
    winning_percentage = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    event_credit = models.CharField(max_length=40, blank=True)
    save_credit = models.CharField(max_length=40, blank=True)
    batters_doubles_against = models.IntegerField(blank=True, null=True)
    batters_triples_against = models.IntegerField(blank=True, null=True)
    outs_recorded = models.IntegerField(blank=True, null=True)
    batters_at_bats_against = models.IntegerField(blank=True, null=True)
    number_of_strikes = models.IntegerField(blank=True, null=True)
    wins_season = models.IntegerField(blank=True, null=True)
    losses_season = models.IntegerField(blank=True, null=True)
    saves_season = models.IntegerField(blank=True, null=True)
    saves_blown_season = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'baseball_pitching_stats'

class BasketballDefensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    steals_total = models.CharField(max_length=100, blank=True)
    steals_per_game = models.CharField(max_length=100, blank=True)
    blocks_total = models.CharField(max_length=100, blank=True)
    blocks_per_game = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'basketball_defensive_stats'

class BasketballEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey('Events')
    current_state = models.IntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    period_value = models.CharField(max_length=100, blank=True)
    period_time_elapsed = models.CharField(max_length=100, blank=True)
    period_time_remaining = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'basketball_event_states'

class BasketballOffensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    field_goals_made = models.IntegerField(blank=True, null=True)
    field_goals_attempted = models.IntegerField(blank=True, null=True)
    field_goals_percentage = models.CharField(max_length=100, blank=True)
    field_goals_per_game = models.CharField(max_length=100, blank=True)
    field_goals_attempted_per_game = models.CharField(max_length=100, blank=True)
    field_goals_percentage_adjusted = models.CharField(max_length=100, blank=True)
    three_pointers_made = models.IntegerField(blank=True, null=True)
    three_pointers_attempted = models.IntegerField(blank=True, null=True)
    three_pointers_percentage = models.CharField(max_length=100, blank=True)
    three_pointers_per_game = models.CharField(max_length=100, blank=True)
    three_pointers_attempted_per_game = models.CharField(max_length=100, blank=True)
    free_throws_made = models.CharField(max_length=100, blank=True)
    free_throws_attempted = models.CharField(max_length=100, blank=True)
    free_throws_percentage = models.CharField(max_length=100, blank=True)
    free_throws_per_game = models.CharField(max_length=100, blank=True)
    free_throws_attempted_per_game = models.CharField(max_length=100, blank=True)
    points_scored_total = models.CharField(max_length=100, blank=True)
    points_scored_per_game = models.CharField(max_length=100, blank=True)
    assists_total = models.CharField(max_length=100, blank=True)
    assists_per_game = models.CharField(max_length=100, blank=True)
    turnovers_total = models.CharField(max_length=100, blank=True)
    turnovers_per_game = models.CharField(max_length=100, blank=True)
    points_scored_off_turnovers = models.CharField(max_length=100, blank=True)
    points_scored_in_paint = models.CharField(max_length=100, blank=True)
    points_scored_on_second_chance = models.CharField(max_length=100, blank=True)
    points_scored_on_fast_break = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'basketball_offensive_stats'

class BasketballReboundingStats(models.Model):
    id = models.IntegerField(primary_key=True)
    rebounds_total = models.CharField(max_length=100, blank=True)
    rebounds_per_game = models.CharField(max_length=100, blank=True)
    rebounds_defensive = models.CharField(max_length=100, blank=True)
    rebounds_offensive = models.CharField(max_length=100, blank=True)
    team_rebounds_total = models.CharField(max_length=100, blank=True)
    team_rebounds_per_game = models.CharField(max_length=100, blank=True)
    team_rebounds_defensive = models.CharField(max_length=100, blank=True)
    team_rebounds_offensive = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'basketball_rebounding_stats'

class BasketballTeamStats(models.Model):
    id = models.IntegerField(primary_key=True)
    timeouts_left = models.CharField(max_length=100, blank=True)
    largest_lead = models.CharField(max_length=100, blank=True)
    fouls_total = models.CharField(max_length=100, blank=True)
    turnover_margin = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'basketball_team_stats'

class Bookmakers(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker_key = models.CharField(max_length=100, blank=True)
    publisher = models.ForeignKey('Publishers')
    location = models.ForeignKey('Locations', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'bookmakers'

class CoreStats(models.Model):
    id = models.IntegerField(primary_key=True)
    score = models.CharField(max_length=100, blank=True)
    score_opposing = models.CharField(max_length=100, blank=True)
    score_attempts = models.CharField(max_length=100, blank=True)
    score_attempts_opposing = models.CharField(max_length=100, blank=True)
    score_percentage = models.CharField(max_length=100, blank=True)
    score_percentage_opposing = models.CharField(max_length=100, blank=True)
    time_played_event = models.CharField(max_length=40, blank=True)
    time_played_total = models.CharField(max_length=40, blank=True)
    time_played_event_average = models.CharField(max_length=40, blank=True)
    events_played = models.CharField(max_length=40, blank=True)
    events_started = models.CharField(max_length=40, blank=True)
    position_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'core_stats'

class DbInfo(models.Model):
    version = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'db_info'

class DisplayNames(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=100)
    entity_id = models.IntegerField()
    full_name = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    alias = models.CharField(max_length=100, blank=True)
    abbreviation = models.CharField(max_length=100, blank=True)
    short_name = models.CharField(max_length=100, blank=True)
    prefix = models.CharField(max_length=20, blank=True)
    suffix = models.CharField(max_length=20, blank=True)
    class Meta:
        managed = False
        db_table = 'display_names'

class DocumentClasses(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'document_classes'

class DocumentContents(models.Model):
    id = models.IntegerField(primary_key=True)
    document = models.ForeignKey('Documents')
    sportsml = models.CharField(max_length=200, blank=True)
    sportsml_blob = models.TextField(blank=True)
    abstract = models.TextField(blank=True)
    abstract_blob = models.TextField(blank=True)
    class Meta:
        managed = False
        db_table = 'document_contents'

class DocumentFixtures(models.Model):
    id = models.IntegerField(primary_key=True)
    fixture_key = models.CharField(max_length=100, blank=True)
    publisher = models.ForeignKey('Publishers')
    name = models.CharField(max_length=100, blank=True)
    document_class = models.ForeignKey(DocumentClasses)
    class Meta:
        managed = False
        db_table = 'document_fixtures'

class DocumentFixturesEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    document_fixture = models.ForeignKey(DocumentFixtures)
    event = models.ForeignKey('Events')
    latest_document = models.ForeignKey('Documents')
    last_update = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'document_fixtures_events'

class DocumentPackageEntry(models.Model):
    id = models.IntegerField(primary_key=True)
    document_package = models.ForeignKey('DocumentPackages')
    rank = models.CharField(max_length=100, blank=True)
    document = models.ForeignKey('Documents')
    headline = models.CharField(max_length=100, blank=True)
    short_headline = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'document_package_entry'

class DocumentPackages(models.Model):
    id = models.IntegerField(primary_key=True)
    package_key = models.CharField(max_length=100, blank=True)
    package_name = models.CharField(max_length=100, blank=True)
    date_time = models.DateField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'document_packages'

class Documents(models.Model):
    id = models.IntegerField(primary_key=True)
    doc_id = models.CharField(max_length=75)
    publisher = models.ForeignKey('Publishers')
    date_time = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=100, blank=True)
    priority = models.CharField(max_length=100, blank=True)
    revision_id = models.CharField(max_length=255, blank=True)
    stats_coverage = models.CharField(max_length=100, blank=True)
    document_fixture = models.ForeignKey(DocumentFixtures)
    source = models.ForeignKey('Publishers', blank=True, null=True)
    db_loading_date_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'documents'

class DocumentsMedia(models.Model):
    id = models.IntegerField(primary_key=True)
    document = models.ForeignKey(Documents)
    media = models.ForeignKey('Media')
    media_caption = models.ForeignKey('MediaCaptions')
    class Meta:
        managed = False
        db_table = 'documents_media'

class EventActionFouls(models.Model):
    id = models.IntegerField(primary_key=True)
    event_state = models.ForeignKey('EventStates')
    foul_name = models.CharField(max_length=100, blank=True)
    foul_result = models.CharField(max_length=100, blank=True)
    foul_type = models.CharField(max_length=100, blank=True)
    fouler_id = models.CharField(max_length=100, blank=True)
    recipient_type = models.CharField(max_length=100, blank=True)
    recipient_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'event_action_fouls'

class EventActionParticipants(models.Model):
    id = models.IntegerField(primary_key=True)
    event_state = models.ForeignKey('EventStates')
    event_action_play = models.ForeignKey('EventActionPlays')
    person = models.ForeignKey('Persons')
    participant_role = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'event_action_participants'

class EventActionPenalties(models.Model):
    id = models.IntegerField(primary_key=True)
    event_state = models.ForeignKey('EventStates')
    penalty_type = models.CharField(max_length=100, blank=True)
    penalty_level = models.CharField(max_length=100, blank=True)
    caution_level = models.CharField(max_length=100, blank=True)
    recipient_type = models.CharField(max_length=100, blank=True)
    recipient_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'event_action_penalties'

class EventActionPlays(models.Model):
    id = models.IntegerField(primary_key=True)
    event_state = models.ForeignKey('EventStates')
    play_type = models.CharField(max_length=100, blank=True)
    score_attempt_type = models.CharField(max_length=100, blank=True)
    play_result = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'event_action_plays'

class EventActionSubstitutions(models.Model):
    id = models.IntegerField(primary_key=True)
    event_state = models.ForeignKey('EventStates')
    person_original = models.ForeignKey('Persons')
    person_original_position = models.ForeignKey('Positions')
    person_replacing = models.ForeignKey('Persons')
    person_replacing_position = models.ForeignKey('Positions')
    substitution_reason = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'event_action_substitutions'

class EventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey('Events')
    current_state = models.IntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    period_value = models.CharField(max_length=100, blank=True)
    period_time_elapsed = models.CharField(max_length=100, blank=True)
    period_time_remaining = models.CharField(max_length=100, blank=True)
    minutes_elapsed = models.CharField(max_length=100, blank=True)
    period_minutes_elapsed = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'event_states'

class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    event_key = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publishers')
    start_date_time = models.DateTimeField(blank=True, null=True)
    site = models.ForeignKey('Sites', blank=True, null=True)
    site_alignment = models.CharField(max_length=100, blank=True)
    event_status = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    attendance = models.CharField(max_length=100, blank=True)
    last_update = models.DateTimeField(blank=True, null=True)
    event_number = models.CharField(max_length=32, blank=True)
    round_number = models.CharField(max_length=32, blank=True)
    time_certainty = models.CharField(max_length=100, blank=True)
    broadcast_listing = models.CharField(max_length=255, blank=True)
    start_date_time_local = models.DateTimeField(blank=True, null=True)
    medal_event = models.CharField(max_length=100, blank=True)
    series_index = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'events'

class EventsDocuments(models.Model):
    event = models.ForeignKey(Events)
    document = models.ForeignKey(Documents)
    class Meta:
        managed = False
        db_table = 'events_documents'

class EventsMedia(models.Model):
    event = models.ForeignKey(Events)
    media = models.ForeignKey('Media')
    class Meta:
        managed = False
        db_table = 'events_media'

class EventsSubSeasons(models.Model):
    event = models.ForeignKey(Events)
    sub_season = models.ForeignKey('SubSeasons')
    class Meta:
        managed = False
        db_table = 'events_sub_seasons'

class IceHockeyActionParticipants(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.ForeignKey('Teams')
    ice_hockey_action_play = models.ForeignKey('IceHockeyActionPlays')
    person = models.ForeignKey('Persons')
    participant_role = models.CharField(max_length=100, blank=True)
    point_credit = models.IntegerField(blank=True, null=True)
    goals_cumulative = models.IntegerField(blank=True, null=True)
    assists_cumulative = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_action_participants'

class IceHockeyActionPlays(models.Model):
    id = models.IntegerField(primary_key=True)
    ice_hockey_event_state = models.ForeignKey('IceHockeyEventStates')
    play_key = models.CharField(max_length=100, blank=True)
    play_type = models.CharField(max_length=100, blank=True)
    score_attempt_type = models.CharField(max_length=100, blank=True)
    play_result = models.CharField(max_length=100, blank=True)
    penalty_type = models.CharField(max_length=100, blank=True)
    penalty_length = models.CharField(max_length=100, blank=True)
    penalty_code = models.CharField(max_length=100, blank=True)
    recipient_type = models.CharField(max_length=100, blank=True)
    team_id = models.IntegerField(blank=True, null=True)
    strength = models.CharField(max_length=100, blank=True)
    shootout_shot_order = models.IntegerField(blank=True, null=True)
    goal_order = models.IntegerField(blank=True, null=True)
    shot_type = models.CharField(max_length=100, blank=True)
    shot_distance = models.CharField(max_length=100, blank=True)
    goal_zone = models.CharField(max_length=100, blank=True)
    penalty_time_remaining = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=40, blank=True)
    zone = models.CharField(max_length=40, blank=True)
    comment = models.CharField(max_length=1024, blank=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_action_plays'

class IceHockeyDefensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    goals_power_play_allowed = models.CharField(max_length=100, blank=True)
    goals_penalty_shot_allowed = models.CharField(max_length=100, blank=True)
    goals_empty_net_allowed = models.CharField(max_length=100, blank=True)
    goals_against_average = models.CharField(max_length=100, blank=True)
    goals_short_handed_allowed = models.CharField(max_length=100, blank=True)
    goals_shootout_allowed = models.CharField(max_length=100, blank=True)
    shots_power_play_allowed = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_allowed = models.CharField(max_length=100, blank=True)
    shots_blocked = models.CharField(max_length=100, blank=True)
    saves = models.CharField(max_length=100, blank=True)
    save_percentage = models.CharField(max_length=100, blank=True)
    penalty_killing_amount = models.CharField(max_length=100, blank=True)
    penalty_killing_percentage = models.CharField(max_length=100, blank=True)
    takeaways = models.CharField(max_length=100, blank=True)
    shutouts = models.CharField(max_length=100, blank=True)
    minutes_penalty_killing = models.CharField(max_length=100, blank=True)
    hits = models.CharField(max_length=100, blank=True)
    shots_shootout_allowed = models.CharField(max_length=100, blank=True)
    goaltender_wins = models.IntegerField(blank=True, null=True)
    goaltender_losses = models.IntegerField(blank=True, null=True)
    goaltender_ties = models.IntegerField(blank=True, null=True)
    goals_allowed = models.IntegerField(blank=True, null=True)
    shots_allowed = models.IntegerField(blank=True, null=True)
    player_count = models.IntegerField(blank=True, null=True)
    player_count_opposing = models.IntegerField(blank=True, null=True)
    goaltender_wins_overtime = models.IntegerField(blank=True, null=True)
    goaltender_losses_overtime = models.IntegerField(blank=True, null=True)
    goals_overtime_allowed = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_defensive_stats'

class IceHockeyEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    power_play_team = models.ForeignKey('Teams', blank=True, null=True)
    event = models.ForeignKey(Events)
    current_state = models.IntegerField(blank=True, null=True)
    period_value = models.CharField(max_length=100, blank=True)
    period_time_elapsed = models.CharField(max_length=100, blank=True)
    period_time_remaining = models.CharField(max_length=100, blank=True)
    record_type = models.CharField(max_length=40, blank=True)
    power_play_player_advantage = models.IntegerField(blank=True, null=True)
    score_team = models.IntegerField(blank=True, null=True)
    score_team_opposing = models.IntegerField(blank=True, null=True)
    score_team_home = models.IntegerField(blank=True, null=True)
    score_team_away = models.IntegerField(blank=True, null=True)
    action_key = models.CharField(max_length=100, blank=True)
    sequence_number = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_event_states'

class IceHockeyFaceoffStats(models.Model):
    id = models.IntegerField(primary_key=True)
    player_count = models.IntegerField(blank=True, null=True)
    player_count_opposing = models.IntegerField(blank=True, null=True)
    faceoff_wins = models.IntegerField(blank=True, null=True)
    faceoff_losses = models.IntegerField(blank=True, null=True)
    faceoff_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_power_play_wins = models.IntegerField(blank=True, null=True)
    faceoffs_power_play_losses = models.IntegerField(blank=True, null=True)
    faceoffs_power_play_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_short_handed_wins = models.IntegerField(blank=True, null=True)
    faceoffs_short_handed_losses = models.IntegerField(blank=True, null=True)
    faceoffs_short_handed_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_even_strength_wins = models.IntegerField(blank=True, null=True)
    faceoffs_even_strength_losses = models.IntegerField(blank=True, null=True)
    faceoffs_even_strength_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_offensive_zone_wins = models.IntegerField(blank=True, null=True)
    faceoffs_offensive_zone_losses = models.IntegerField(blank=True, null=True)
    faceoffs_offensive_zone_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_defensive_zone_wins = models.IntegerField(blank=True, null=True)
    faceoffs_defensive_zone_losses = models.IntegerField(blank=True, null=True)
    faceoffs_defensive_zone_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    faceoffs_neutral_zone_wins = models.IntegerField(blank=True, null=True)
    faceoffs_neutral_zone_losses = models.IntegerField(blank=True, null=True)
    faceoffs_neutral_zone_win_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_faceoff_stats'

class IceHockeyOffensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    giveaways = models.CharField(max_length=100, blank=True)
    goals = models.IntegerField(blank=True, null=True)
    goals_game_winning = models.CharField(max_length=100, blank=True)
    goals_game_tying = models.CharField(max_length=100, blank=True)
    goals_power_play = models.CharField(max_length=100, blank=True)
    goals_short_handed = models.CharField(max_length=100, blank=True)
    goals_even_strength = models.CharField(max_length=100, blank=True)
    goals_empty_net = models.CharField(max_length=100, blank=True)
    goals_overtime = models.CharField(max_length=100, blank=True)
    goals_shootout = models.CharField(max_length=100, blank=True)
    goals_penalty_shot = models.CharField(max_length=100, blank=True)
    assists = models.CharField(max_length=100, blank=True)
    shots = models.IntegerField(blank=True, null=True)
    shots_penalty_shot_taken = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_missed = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_percentage = models.CharField(max_length=100, blank=True)
    shots_missed = models.IntegerField(blank=True, null=True)
    shots_blocked = models.IntegerField(blank=True, null=True)
    shots_power_play = models.IntegerField(blank=True, null=True)
    shots_short_handed = models.IntegerField(blank=True, null=True)
    shots_even_strength = models.IntegerField(blank=True, null=True)
    points = models.CharField(max_length=100, blank=True)
    power_play_amount = models.CharField(max_length=100, blank=True)
    power_play_percentage = models.CharField(max_length=100, blank=True)
    minutes_power_play = models.CharField(max_length=100, blank=True)
    faceoff_wins = models.CharField(max_length=100, blank=True)
    faceoff_losses = models.CharField(max_length=100, blank=True)
    faceoff_win_percentage = models.CharField(max_length=100, blank=True)
    scoring_chances = models.CharField(max_length=100, blank=True)
    player_count = models.IntegerField(blank=True, null=True)
    player_count_opposing = models.IntegerField(blank=True, null=True)
    assists_game_winning = models.IntegerField(blank=True, null=True)
    assists_overtime = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_offensive_stats'

class IceHockeyPlayerStats(models.Model):
    id = models.IntegerField(primary_key=True)
    plus_minus = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_player_stats'

class IceHockeyTimeOnIceStats(models.Model):
    id = models.IntegerField(primary_key=True)
    player_count = models.IntegerField(blank=True, null=True)
    player_count_opposing = models.IntegerField(blank=True, null=True)
    shifts = models.IntegerField(blank=True, null=True)
    time_total = models.CharField(max_length=40, blank=True)
    time_power_play = models.CharField(max_length=40, blank=True)
    time_short_handed = models.CharField(max_length=40, blank=True)
    time_even_strength = models.CharField(max_length=40, blank=True)
    time_empty_net = models.CharField(max_length=40, blank=True)
    time_power_play_empty_net = models.CharField(max_length=40, blank=True)
    time_short_handed_empty_net = models.CharField(max_length=40, blank=True)
    time_even_strength_empty_net = models.CharField(max_length=40, blank=True)
    time_average_per_shift = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'ice_hockey_time_on_ice_stats'

class InjuryPhases(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Persons')
    injury_status = models.CharField(max_length=100, blank=True)
    injury_type = models.CharField(max_length=100, blank=True)
    injury_comment = models.CharField(max_length=100, blank=True)
    disabled_list = models.CharField(max_length=100, blank=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    season = models.ForeignKey('Seasons', blank=True, null=True)
    phase_type = models.CharField(max_length=100, blank=True)
    injury_side = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'injury_phases'

class KeyAliases(models.Model):
    id = models.IntegerField(primary_key=True)
    key_id = models.IntegerField()
    key_root = models.ForeignKey('KeyRoots')
    class Meta:
        managed = False
        db_table = 'key_aliases'

class KeyRoots(models.Model):
    id = models.IntegerField(primary_key=True)
    key_type = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'key_roots'

class LatestRevisions(models.Model):
    id = models.IntegerField(primary_key=True)
    revision_id = models.CharField(max_length=255)
    latest_document = models.ForeignKey(Documents)
    class Meta:
        managed = False
        db_table = 'latest_revisions'

class Locations(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    area = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    timezone = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    country_code = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'locations'

class Media(models.Model):
    id = models.IntegerField(primary_key=True)
    object_id = models.IntegerField(blank=True, null=True)
    source_id = models.IntegerField(blank=True, null=True)
    revision_id = models.IntegerField(blank=True, null=True)
    media_type = models.CharField(max_length=100, blank=True)
    publisher = models.ForeignKey('Publishers')
    date_time = models.CharField(max_length=100, blank=True)
    credit = models.ForeignKey('Persons')
    db_loading_date_time = models.DateTimeField(blank=True, null=True)
    creation_location = models.ForeignKey(Locations)
    class Meta:
        managed = False
        db_table = 'media'

class MediaCaptions(models.Model):
    id = models.IntegerField(primary_key=True)
    media = models.ForeignKey(Media)
    caption_type = models.CharField(max_length=100, blank=True)
    caption = models.CharField(max_length=100, blank=True)
    caption_author = models.ForeignKey('Persons')
    language = models.CharField(max_length=100, blank=True)
    caption_size = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'media_captions'

class MediaContents(models.Model):
    id = models.IntegerField(primary_key=True)
    media = models.ForeignKey(Media)
    object = models.CharField(max_length=100, blank=True)
    format = models.CharField(max_length=100, blank=True)
    mime_type = models.CharField(max_length=100, blank=True)
    height = models.CharField(max_length=100, blank=True)
    width = models.CharField(max_length=100, blank=True)
    duration = models.CharField(max_length=100, blank=True)
    file_size = models.CharField(max_length=100, blank=True)
    resolution = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'media_contents'

class MediaKeywords(models.Model):
    id = models.IntegerField(primary_key=True)
    keyword = models.CharField(max_length=100, blank=True)
    media = models.ForeignKey(Media)
    class Meta:
        managed = False
        db_table = 'media_keywords'

class MotorRacingEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events)
    current_state = models.IntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    lap = models.CharField(max_length=100, blank=True)
    laps_remaining = models.CharField(max_length=100, blank=True)
    time_elapsed = models.CharField(max_length=100, blank=True)
    flag_state = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'motor_racing_event_states'

class MotorRacingEventStats(models.Model):
    id = models.IntegerField(primary_key=True)
    speed_average = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    speed_units = models.CharField(max_length=40, blank=True)
    margin_of_victory = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    caution_flags = models.IntegerField(blank=True, null=True)
    caution_flags_laps = models.IntegerField(blank=True, null=True)
    lead_changes = models.IntegerField(blank=True, null=True)
    lead_changes_drivers = models.IntegerField(blank=True, null=True)
    laps_total = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'motor_racing_event_stats'

class MotorRacingQualifyingStats(models.Model):
    id = models.IntegerField(primary_key=True)
    grid = models.CharField(max_length=100, blank=True)
    pole_position = models.CharField(max_length=100, blank=True)
    pole_wins = models.CharField(max_length=100, blank=True)
    qualifying_speed = models.CharField(max_length=100, blank=True)
    qualifying_speed_units = models.CharField(max_length=100, blank=True)
    qualifying_time = models.CharField(max_length=100, blank=True)
    qualifying_position = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'motor_racing_qualifying_stats'

class MotorRacingRaceStats(models.Model):
    id = models.IntegerField(primary_key=True)
    time_behind_leader = models.CharField(max_length=100, blank=True)
    laps_behind_leader = models.CharField(max_length=100, blank=True)
    time_ahead_follower = models.CharField(max_length=100, blank=True)
    laps_ahead_follower = models.CharField(max_length=100, blank=True)
    time = models.CharField(max_length=100, blank=True)
    points = models.CharField(max_length=100, blank=True)
    points_rookie = models.CharField(max_length=100, blank=True)
    bonus = models.CharField(max_length=100, blank=True)
    laps_completed = models.CharField(max_length=100, blank=True)
    laps_leading_total = models.CharField(max_length=100, blank=True)
    distance_leading = models.CharField(max_length=100, blank=True)
    distance_completed = models.CharField(max_length=100, blank=True)
    distance_units = models.CharField(max_length=40, blank=True)
    speed_average = models.CharField(max_length=40, blank=True)
    speed_units = models.CharField(max_length=40, blank=True)
    status = models.CharField(max_length=40, blank=True)
    finishes_top_5 = models.CharField(max_length=40, blank=True)
    finishes_top_10 = models.CharField(max_length=40, blank=True)
    starts = models.CharField(max_length=40, blank=True)
    finishes = models.CharField(max_length=40, blank=True)
    non_finishes = models.CharField(max_length=40, blank=True)
    wins = models.CharField(max_length=40, blank=True)
    races_leading = models.CharField(max_length=40, blank=True)
    money = models.CharField(max_length=40, blank=True)
    money_units = models.CharField(max_length=40, blank=True)
    leads_total = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'motor_racing_race_stats'

class OutcomeTotals(models.Model):
    id = models.IntegerField(primary_key=True)
    standing_subgroup = models.ForeignKey('StandingSubgroups')
    outcome_holder_type = models.CharField(max_length=100, blank=True)
    outcome_holder_id = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True)
    wins = models.CharField(max_length=100, blank=True)
    losses = models.CharField(max_length=100, blank=True)
    ties = models.CharField(max_length=100, blank=True)
    wins_overtime = models.IntegerField(blank=True, null=True)
    losses_overtime = models.IntegerField(blank=True, null=True)
    undecideds = models.CharField(max_length=100, blank=True)
    winning_percentage = models.CharField(max_length=100, blank=True)
    points_scored_for = models.CharField(max_length=100, blank=True)
    points_scored_against = models.CharField(max_length=100, blank=True)
    points_difference = models.CharField(max_length=100, blank=True)
    standing_points = models.CharField(max_length=100, blank=True)
    streak_type = models.CharField(max_length=100, blank=True)
    streak_duration = models.CharField(max_length=100, blank=True)
    streak_total = models.CharField(max_length=100, blank=True)
    streak_start = models.DateTimeField(blank=True, null=True)
    streak_end = models.DateTimeField(blank=True, null=True)
    events_played = models.IntegerField(blank=True, null=True)
    games_back = models.CharField(max_length=100, blank=True)
    result_effect = models.CharField(max_length=100, blank=True)
    sets_against = models.CharField(max_length=100, blank=True)
    sets_for = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'outcome_totals'

class ParticipantsEvents(models.Model):
    id = models.IntegerField(primary_key=True)
    participant_type = models.CharField(max_length=100)
    participant_id = models.IntegerField()
    event = models.ForeignKey(Events)
    alignment = models.CharField(max_length=100, blank=True)
    score = models.CharField(max_length=100, blank=True)
    event_outcome = models.CharField(max_length=100, blank=True)
    rank = models.IntegerField(blank=True, null=True)
    result_effect = models.CharField(max_length=100, blank=True)
    score_attempts = models.IntegerField(blank=True, null=True)
    sort_order = models.CharField(max_length=100, blank=True)
    score_type = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'participants_events'

class PenaltyStats(models.Model):
    id = models.IntegerField(primary_key=True)
    count = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=100, blank=True)
    value = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'penalty_stats'

class Periods(models.Model):
    id = models.IntegerField(primary_key=True)
    participant_event = models.ForeignKey(ParticipantsEvents)
    period_value = models.CharField(max_length=100, blank=True)
    score = models.CharField(max_length=100, blank=True)
    score_attempts = models.IntegerField(blank=True, null=True)
    rank = models.CharField(max_length=100, blank=True)
    sub_score_key = models.CharField(max_length=100, blank=True)
    sub_score_type = models.CharField(max_length=100, blank=True)
    sub_score_name = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'periods'

class PersonEventMetadata(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Persons')
    event = models.ForeignKey(Events)
    status = models.CharField(max_length=100, blank=True)
    health = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    role = models.ForeignKey('Roles', blank=True, null=True)
    position = models.ForeignKey('Positions', blank=True, null=True)
    team = models.ForeignKey('Teams', blank=True, null=True)
    lineup_slot = models.IntegerField(blank=True, null=True)
    lineup_slot_sequence = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'person_event_metadata'

class PersonPhases(models.Model):
    id = models.IntegerField(primary_key=True)
    person = models.ForeignKey('Persons')
    membership_type = models.CharField(max_length=40)
    membership_id = models.IntegerField()
    role = models.ForeignKey('Roles', blank=True, null=True)
    role_status = models.CharField(max_length=40, blank=True)
    phase_status = models.CharField(max_length=40, blank=True)
    uniform_number = models.CharField(max_length=20, blank=True)
    regular_position = models.ForeignKey('Positions', blank=True, null=True)
    regular_position_depth = models.CharField(max_length=40, blank=True)
    height = models.CharField(max_length=100, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    start_season = models.ForeignKey('Seasons', blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    end_season = models.ForeignKey('Seasons', blank=True, null=True)
    entry_reason = models.CharField(max_length=40, blank=True)
    exit_reason = models.CharField(max_length=40, blank=True)
    selection_level = models.IntegerField(blank=True, null=True)
    selection_sublevel = models.IntegerField(blank=True, null=True)
    selection_overall = models.IntegerField(blank=True, null=True)
    duration = models.CharField(max_length=32, blank=True)
    phase_type = models.CharField(max_length=40, blank=True)
    subphase_type = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'person_phases'

class Persons(models.Model):
    id = models.IntegerField(primary_key=True)
    person_key = models.CharField(max_length=100)
    publisher = models.ForeignKey('Publishers')
    gender = models.CharField(max_length=20, blank=True)
    birth_date = models.CharField(max_length=30, blank=True)
    death_date = models.CharField(max_length=30, blank=True)
    final_resting_location = models.ForeignKey(Locations, blank=True, null=True)
    birth_location = models.ForeignKey(Locations, blank=True, null=True)
    hometown_location = models.ForeignKey(Locations, blank=True, null=True)
    residence_location = models.ForeignKey(Locations, blank=True, null=True)
    death_location = models.ForeignKey(Locations, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'persons'

class PersonsDocuments(models.Model):
    person = models.ForeignKey(Persons)
    document = models.ForeignKey(Documents)
    class Meta:
        managed = False
        db_table = 'persons_documents'

class PersonsMedia(models.Model):
    person = models.ForeignKey(Persons)
    media = models.ForeignKey(Media)
    class Meta:
        managed = False
        db_table = 'persons_media'

class Positions(models.Model):
    id = models.IntegerField(primary_key=True)
    affiliation = models.ForeignKey(Affiliations)
    abbreviation = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'positions'

class Publishers(models.Model):
    id = models.IntegerField(primary_key=True)
    publisher_key = models.CharField(max_length=100)
    publisher_name = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'publishers'

class Rankings(models.Model):
    id = models.IntegerField(primary_key=True)
    document_fixture_id = models.IntegerField(blank=True, null=True)
    participant_type = models.CharField(max_length=100, blank=True)
    participant_id = models.IntegerField(blank=True, null=True)
    issuer = models.CharField(max_length=100, blank=True)
    ranking_type = models.CharField(max_length=100, blank=True)
    ranking_value = models.CharField(max_length=100, blank=True)
    ranking_value_previous = models.CharField(max_length=100, blank=True)
    date_coverage_type = models.CharField(max_length=100, blank=True)
    date_coverage_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'rankings'

class Records(models.Model):
    id = models.IntegerField(primary_key=True)
    participant_type = models.CharField(max_length=100, blank=True)
    participant_id = models.IntegerField(blank=True, null=True)
    record_type = models.CharField(max_length=100, blank=True)
    record_label = models.CharField(max_length=100, blank=True)
    record_value = models.CharField(max_length=100, blank=True)
    previous_value = models.CharField(max_length=100, blank=True)
    date_coverage_type = models.CharField(max_length=100, blank=True)
    date_coverage_id = models.IntegerField(blank=True, null=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'records'

class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    role_key = models.CharField(max_length=100)
    role_name = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'roles'

class Seasons(models.Model):
    id = models.IntegerField(primary_key=True)
    season_key = models.IntegerField()
    publisher = models.ForeignKey(Publishers)
    league = models.ForeignKey(Affiliations, blank=True, null=True)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'seasons'

class Sites(models.Model):
    id = models.IntegerField(primary_key=True)
    site_key = models.CharField(max_length=128)
    publisher = models.ForeignKey(Publishers)
    location = models.ForeignKey(Locations, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sites'

class SoccerActionFouls(models.Model):
    id = models.IntegerField(primary_key=True)
    soccer_event_state = models.ForeignKey('SoccerEventStates')
    foul_name = models.CharField(max_length=100, blank=True)
    foul_result = models.CharField(max_length=100, blank=True)
    foul_type = models.CharField(max_length=100, blank=True)
    fouler_id = models.CharField(max_length=100, blank=True)
    recipient_type = models.CharField(max_length=100, blank=True)
    recipient = models.ForeignKey(Persons)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_action_fouls'

class SoccerActionParticipants(models.Model):
    id = models.IntegerField(primary_key=True)
    soccer_action_play = models.ForeignKey('SoccerActionPlays')
    person = models.ForeignKey(Persons)
    participant_role = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_action_participants'

class SoccerActionPenalties(models.Model):
    id = models.IntegerField(primary_key=True)
    soccer_event_state = models.ForeignKey('SoccerEventStates')
    penalty_type = models.CharField(max_length=100, blank=True)
    penalty_level = models.CharField(max_length=100, blank=True)
    caution_value = models.CharField(max_length=100, blank=True)
    recipient_type = models.CharField(max_length=100, blank=True)
    recipient = models.ForeignKey(Persons)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_action_penalties'

class SoccerActionPlays(models.Model):
    id = models.IntegerField(primary_key=True)
    soccer_event_state = models.ForeignKey('SoccerEventStates')
    play_type = models.CharField(max_length=100, blank=True)
    score_attempt_type = models.CharField(max_length=100, blank=True)
    play_result = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_action_plays'

class SoccerActionSubstitutions(models.Model):
    id = models.IntegerField(primary_key=True)
    soccer_event_state = models.ForeignKey('SoccerEventStates')
    person_type = models.CharField(max_length=100, blank=True)
    person_original = models.ForeignKey(Persons)
    person_original_position = models.ForeignKey(Positions, blank=True, null=True)
    person_replacing = models.ForeignKey(Persons)
    person_replacing_position = models.ForeignKey(Positions, blank=True, null=True)
    substitution_reason = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=512, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_action_substitutions'

class SoccerDefensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    shots_penalty_shot_allowed = models.CharField(max_length=100, blank=True)
    goals_penalty_shot_allowed = models.CharField(max_length=100, blank=True)
    goals_against_average = models.CharField(max_length=100, blank=True)
    goals_against_total = models.CharField(max_length=100, blank=True)
    saves = models.CharField(max_length=100, blank=True)
    save_percentage = models.CharField(max_length=100, blank=True)
    catches_punches = models.CharField(max_length=100, blank=True)
    shots_on_goal_total = models.CharField(max_length=100, blank=True)
    shots_shootout_total = models.CharField(max_length=100, blank=True)
    shots_shootout_allowed = models.CharField(max_length=100, blank=True)
    shots_blocked = models.CharField(max_length=100, blank=True)
    shutouts = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_defensive_stats'

class SoccerEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events)
    current_state = models.IntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    period_value = models.CharField(max_length=100, blank=True)
    period_time_elapsed = models.CharField(max_length=100, blank=True)
    period_time_remaining = models.CharField(max_length=100, blank=True)
    minutes_elapsed = models.CharField(max_length=100, blank=True)
    period_minute_elapsed = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'soccer_event_states'

class SoccerFoulStats(models.Model):
    id = models.IntegerField(primary_key=True)
    fouls_suffered = models.CharField(max_length=100, blank=True)
    fouls_commited = models.CharField(max_length=100, blank=True)
    cautions_total = models.CharField(max_length=100, blank=True)
    cautions_pending = models.CharField(max_length=100, blank=True)
    caution_points_total = models.CharField(max_length=100, blank=True)
    caution_points_pending = models.CharField(max_length=100, blank=True)
    ejections_total = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_foul_stats'

class SoccerOffensiveStats(models.Model):
    id = models.IntegerField(primary_key=True)
    goals_game_winning = models.CharField(max_length=100, blank=True)
    goals_game_tying = models.CharField(max_length=100, blank=True)
    goals_overtime = models.CharField(max_length=100, blank=True)
    goals_shootout = models.CharField(max_length=100, blank=True)
    goals_total = models.CharField(max_length=100, blank=True)
    assists_game_winning = models.CharField(max_length=100, blank=True)
    assists_game_tying = models.CharField(max_length=100, blank=True)
    assists_overtime = models.CharField(max_length=100, blank=True)
    assists_total = models.CharField(max_length=100, blank=True)
    points = models.CharField(max_length=100, blank=True)
    shots_total = models.CharField(max_length=100, blank=True)
    shots_on_goal_total = models.CharField(max_length=100, blank=True)
    shots_hit_frame = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_taken = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_scored = models.CharField(max_length=100, blank=True)
    shots_penalty_shot_missed = models.CharField(max_length=40, blank=True)
    shots_penalty_shot_percentage = models.CharField(max_length=40, blank=True)
    shots_shootout_taken = models.CharField(max_length=40, blank=True)
    shots_shootout_scored = models.CharField(max_length=40, blank=True)
    shots_shootout_missed = models.CharField(max_length=40, blank=True)
    shots_shootout_percentage = models.CharField(max_length=40, blank=True)
    giveaways = models.CharField(max_length=40, blank=True)
    offsides = models.CharField(max_length=40, blank=True)
    corner_kicks = models.CharField(max_length=40, blank=True)
    hat_tricks = models.CharField(max_length=40, blank=True)
    class Meta:
        managed = False
        db_table = 'soccer_offensive_stats'

class SportsProperty(models.Model):
    id = models.IntegerField(primary_key=True)
    sports_property_type = models.CharField(max_length=100, blank=True)
    sports_property_id = models.IntegerField(blank=True, null=True)
    formal_name = models.CharField(max_length=100)
    value = models.CharField(max_length=255, blank=True)
    class Meta:
        managed = False
        db_table = 'sports_property'

class StandingSubgroups(models.Model):
    id = models.IntegerField(primary_key=True)
    standing = models.ForeignKey('Standings')
    affiliation = models.ForeignKey(Affiliations)
    alignment_scope = models.CharField(max_length=100, blank=True)
    competition_scope = models.CharField(max_length=100, blank=True)
    competition_scope_id = models.CharField(max_length=100, blank=True)
    duration_scope = models.CharField(max_length=100, blank=True)
    scoping_label = models.CharField(max_length=100, blank=True)
    site_scope = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'standing_subgroups'

class Standings(models.Model):
    id = models.IntegerField(primary_key=True)
    affiliation = models.ForeignKey(Affiliations)
    standing_type = models.CharField(max_length=100, blank=True)
    sub_season = models.ForeignKey('SubSeasons')
    last_updated = models.CharField(max_length=100, blank=True)
    source = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'standings'

class Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    stat_repository_type = models.CharField(max_length=100, blank=True)
    stat_repository_id = models.IntegerField()
    stat_holder_type = models.CharField(max_length=100, blank=True)
    stat_holder_id = models.IntegerField(blank=True, null=True)
    stat_coverage_type = models.CharField(max_length=100, blank=True)
    stat_coverage_id = models.IntegerField(blank=True, null=True)
    stat_membership_type = models.CharField(max_length=40, blank=True)
    stat_membership_id = models.IntegerField(blank=True, null=True)
    context = models.CharField(max_length=40)
    class Meta:
        managed = False
        db_table = 'stats'

class SubPeriods(models.Model):
    id = models.IntegerField(primary_key=True)
    period = models.ForeignKey(Periods)
    sub_period_value = models.CharField(max_length=100, blank=True)
    score = models.CharField(max_length=100, blank=True)
    score_attempts = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sub_periods'

class SubSeasons(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_season_key = models.CharField(max_length=100)
    season = models.ForeignKey(Seasons)
    sub_season_type = models.CharField(max_length=100)
    start_date_time = models.DateTimeField(blank=True, null=True)
    end_date_time = models.DateTimeField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'sub_seasons'

class TeamPhases(models.Model):
    id = models.IntegerField(primary_key=True)
    team = models.ForeignKey('Teams')
    start_season = models.ForeignKey(Seasons, blank=True, null=True)
    end_season = models.ForeignKey(Seasons, blank=True, null=True)
    affiliation = models.ForeignKey(Affiliations)
    start_date_time = models.CharField(max_length=100, blank=True)
    end_date_time = models.CharField(max_length=100, blank=True)
    phase_status = models.CharField(max_length=40, blank=True)
    role = models.ForeignKey(Roles, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'team_phases'

class Teams(models.Model):
    id = models.IntegerField(primary_key=True)
    team_key = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publishers)
    home_site = models.ForeignKey(Sites, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'teams'

class TeamsDocuments(models.Model):
    team = models.ForeignKey(Teams)
    document = models.ForeignKey(Documents)
    class Meta:
        managed = False
        db_table = 'teams_documents'

class TeamsMedia(models.Model):
    team = models.ForeignKey(Teams)
    media = models.ForeignKey(Media)
    class Meta:
        managed = False
        db_table = 'teams_media'

class TennisActionPoints(models.Model):
    id = models.IntegerField(primary_key=True)
    sub_period_id = models.CharField(max_length=100, blank=True)
    sequence_number = models.CharField(max_length=100, blank=True)
    win_type = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'tennis_action_points'

class TennisActionVolleys(models.Model):
    id = models.IntegerField(primary_key=True)
    sequence_number = models.CharField(max_length=100, blank=True)
    tennis_action_points_id = models.IntegerField(blank=True, null=True)
    landing_location = models.CharField(max_length=100, blank=True)
    swing_type = models.CharField(max_length=100, blank=True)
    result = models.CharField(max_length=100, blank=True)
    spin_type = models.CharField(max_length=100, blank=True)
    trajectory_details = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'tennis_action_volleys'

class TennisEventStates(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events)
    current_state = models.IntegerField(blank=True, null=True)
    sequence_number = models.IntegerField(blank=True, null=True)
    tennis_set = models.CharField(max_length=100, blank=True)
    game = models.CharField(max_length=100, blank=True)
    server_person_id = models.IntegerField(blank=True, null=True)
    server_score = models.CharField(max_length=100, blank=True)
    receiver_person_id = models.IntegerField(blank=True, null=True)
    receiver_score = models.CharField(max_length=100, blank=True)
    service_number = models.CharField(max_length=100, blank=True)
    context = models.CharField(max_length=40, blank=True)
    document_id = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_event_states'

class TennisPlayerStats(models.Model):
    id = models.IntegerField(primary_key=True)
    net_points_won = models.IntegerField(blank=True, null=True)
    net_points_played = models.IntegerField(blank=True, null=True)
    points_won = models.IntegerField(blank=True, null=True)
    winners = models.IntegerField(blank=True, null=True)
    unforced_errors = models.IntegerField(blank=True, null=True)
    winners_forehand = models.IntegerField(blank=True, null=True)
    winners_backhand = models.IntegerField(blank=True, null=True)
    winners_volley = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_player_stats'

class TennisReturnStats(models.Model):
    id = models.IntegerField(primary_key=True)
    returns_played = models.IntegerField(blank=True, null=True)
    matches_played = models.IntegerField(blank=True, null=True)
    first_service_return_points_won = models.IntegerField(blank=True, null=True)
    first_service_return_points_won_pct = models.IntegerField(blank=True, null=True)
    second_service_return_points_won = models.IntegerField(blank=True, null=True)
    second_service_return_points_won_pct = models.IntegerField(blank=True, null=True)
    return_games_played = models.IntegerField(blank=True, null=True)
    return_games_won = models.IntegerField(blank=True, null=True)
    return_games_won_pct = models.IntegerField(blank=True, null=True)
    break_points_played = models.IntegerField(blank=True, null=True)
    break_points_converted = models.IntegerField(blank=True, null=True)
    break_points_converted_pct = models.IntegerField(blank=True, null=True)
    net_points_won = models.IntegerField(blank=True, null=True)
    net_points_played = models.IntegerField(blank=True, null=True)
    points_won = models.IntegerField(blank=True, null=True)
    winners = models.IntegerField(blank=True, null=True)
    unforced_errors = models.IntegerField(blank=True, null=True)
    winners_forehand = models.IntegerField(blank=True, null=True)
    winners_backhand = models.IntegerField(blank=True, null=True)
    winners_volley = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_return_stats'

class TennisServiceStats(models.Model):
    id = models.IntegerField(primary_key=True)
    services_played = models.IntegerField(blank=True, null=True)
    matches_played = models.IntegerField(blank=True, null=True)
    aces = models.IntegerField(blank=True, null=True)
    first_services_good = models.IntegerField(blank=True, null=True)
    first_services_good_pct = models.IntegerField(blank=True, null=True)
    first_service_points_won = models.IntegerField(blank=True, null=True)
    first_service_points_won_pct = models.IntegerField(blank=True, null=True)
    second_service_points_won = models.IntegerField(blank=True, null=True)
    second_service_points_won_pct = models.IntegerField(blank=True, null=True)
    service_games_played = models.IntegerField(blank=True, null=True)
    service_games_won = models.IntegerField(blank=True, null=True)
    service_games_won_pct = models.IntegerField(blank=True, null=True)
    break_points_played = models.IntegerField(blank=True, null=True)
    break_points_saved = models.IntegerField(blank=True, null=True)
    break_points_saved_pct = models.IntegerField(blank=True, null=True)
    service_points_won = models.IntegerField(blank=True, null=True)
    service_points_won_pct = models.IntegerField(blank=True, null=True)
    double_faults = models.IntegerField(blank=True, null=True)
    first_service_top_speed = models.CharField(max_length=100, blank=True)
    second_services_good = models.IntegerField(blank=True, null=True)
    second_services_good_pct = models.IntegerField(blank=True, null=True)
    second_service_top_speed = models.CharField(max_length=100, blank=True)
    net_points_won = models.IntegerField(blank=True, null=True)
    net_points_played = models.IntegerField(blank=True, null=True)
    points_won = models.IntegerField(blank=True, null=True)
    winners = models.IntegerField(blank=True, null=True)
    unforced_errors = models.IntegerField(blank=True, null=True)
    winners_forehand = models.IntegerField(blank=True, null=True)
    winners_backhand = models.IntegerField(blank=True, null=True)
    winners_volley = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_service_stats'

class TennisSetStats(models.Model):
    id = models.IntegerField(primary_key=True)
    net_points_won = models.IntegerField(blank=True, null=True)
    net_points_played = models.IntegerField(blank=True, null=True)
    points_won = models.IntegerField(blank=True, null=True)
    winners = models.IntegerField(blank=True, null=True)
    unforced_errors = models.IntegerField(blank=True, null=True)
    winners_forehand = models.IntegerField(blank=True, null=True)
    winners_backhand = models.IntegerField(blank=True, null=True)
    winners_volley = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_set_stats'

class TennisTeamStats(models.Model):
    id = models.IntegerField(primary_key=True)
    net_points_won = models.IntegerField(blank=True, null=True)
    net_points_played = models.IntegerField(blank=True, null=True)
    points_won = models.IntegerField(blank=True, null=True)
    winners = models.IntegerField(blank=True, null=True)
    unforced_errors = models.IntegerField(blank=True, null=True)
    winners_forehand = models.IntegerField(blank=True, null=True)
    winners_backhand = models.IntegerField(blank=True, null=True)
    winners_volley = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'tennis_team_stats'

class WageringMoneylines(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker = models.ForeignKey(Bookmakers)
    event = models.ForeignKey(Events)
    date_time = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(Teams)
    person_id = models.IntegerField(blank=True, null=True)
    rotation_key = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    vigorish = models.CharField(max_length=100, blank=True)
    line = models.CharField(max_length=100, blank=True)
    line_opening = models.CharField(max_length=100, blank=True)
    prediction = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wagering_moneylines'

class WageringOddsLines(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker = models.ForeignKey(Bookmakers)
    event = models.ForeignKey(Events)
    date_time = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(Teams)
    person_id = models.IntegerField(blank=True, null=True)
    rotation_key = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    numerator = models.CharField(max_length=100, blank=True)
    denominator = models.CharField(max_length=100, blank=True)
    prediction = models.CharField(max_length=100, blank=True)
    payout_calculation = models.CharField(max_length=100, blank=True)
    payout_amount = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wagering_odds_lines'

class WageringRunlines(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker = models.ForeignKey(Bookmakers)
    event = models.ForeignKey(Events)
    date_time = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(Teams)
    person_id = models.IntegerField(blank=True, null=True)
    rotation_key = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    vigorish = models.CharField(max_length=100, blank=True)
    line = models.CharField(max_length=100, blank=True)
    line_opening = models.CharField(max_length=100, blank=True)
    line_value = models.CharField(max_length=100, blank=True)
    prediction = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wagering_runlines'

class WageringStraightSpreadLines(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker = models.ForeignKey(Bookmakers)
    event = models.ForeignKey(Events)
    date_time = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(Teams)
    person_id = models.IntegerField(blank=True, null=True)
    rotation_key = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    vigorish = models.CharField(max_length=100, blank=True)
    line_value = models.CharField(max_length=100, blank=True)
    line_value_opening = models.CharField(max_length=100, blank=True)
    prediction = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wagering_straight_spread_lines'

class WageringTotalScoreLines(models.Model):
    id = models.IntegerField(primary_key=True)
    bookmaker = models.ForeignKey(Bookmakers)
    event = models.ForeignKey(Events)
    date_time = models.DateTimeField(blank=True, null=True)
    team = models.ForeignKey(Teams)
    person_id = models.IntegerField(blank=True, null=True)
    rotation_key = models.CharField(max_length=100, blank=True)
    comment = models.CharField(max_length=255, blank=True)
    vigorish = models.CharField(max_length=100, blank=True)
    line_over = models.CharField(max_length=100, blank=True)
    line_under = models.CharField(max_length=100, blank=True)
    total = models.CharField(max_length=100, blank=True)
    total_opening = models.CharField(max_length=100, blank=True)
    prediction = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'wagering_total_score_lines'

class WeatherConditions(models.Model):
    id = models.IntegerField(primary_key=True)
    event = models.ForeignKey(Events)
    temperature = models.CharField(max_length=100, blank=True)
    temperature_units = models.CharField(max_length=40, blank=True)
    humidity = models.CharField(max_length=100, blank=True)
    clouds = models.CharField(max_length=100, blank=True)
    wind_direction = models.CharField(max_length=100, blank=True)
    wind_velocity = models.CharField(max_length=100, blank=True)
    weather_code = models.CharField(max_length=100, blank=True)
    class Meta:
        managed = False
        db_table = 'weather_conditions'

