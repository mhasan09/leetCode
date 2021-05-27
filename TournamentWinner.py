def updateScores(team, scoreValue, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += scoreValue


def TournamentWinner(competitions, results):
    HOME_TEAM_WINS = 1
    currentBestTeam = ''
    scores = {currentBestTeam: 0}
    for index, item in enumerate(competitions):
        homeTeam, awayTeam = item
        result = results[index]
        if result == HOME_TEAM_WINS:
            winningTeam = homeTeam
        else:
            winningTeam = awayTeam
        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam
    print(scores)
    return currentBestTeam


print(TournamentWinner([["HTML", "C#"],
                        ["Python", "C#"],
                        ["Python", "HTML"]], [0, 0, 1])
      )
