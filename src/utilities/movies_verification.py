class MoviesVerification:
    def verify_winner_value(data):
        """
        Verifies the value of 'winner' in the provided data.

        Args:
            data (dict): Dictionary containing movie data.

        Returns:
            bool: True if 'winner' exists and is 'yes', otherwise returns False.
        """
                
        # Verifies if winner exist in data. If not, set winner as False.
        if data.get('winner'):
            winner_value = str(data['winner']).lower() == 'yes'
        else:
            winner_value = False
    
        return winner_value