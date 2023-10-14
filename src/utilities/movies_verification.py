class MoviesVerification:
    def verify_winner_value(data):
        if data.get('winner'):
            winner_value = data['winner'].lower() == 'yes'
        else:
            winner_value = False
    
        return winner_value