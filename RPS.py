# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

winning_combinations = {'R': 'P', 'P': 'S', 'S': 'R'}

def player(prev_play, opponent_history=[]):
  if prev_play != '': 
    opponent_history.append(prev_play)
  else:
    opponent_history.clear()
    

  n = 4
  guess = "R"
     
  if len(opponent_history) >= n:
    
    pattern = [ ''.join(opponent_history[k:k+n]) for k, v  in enumerate(opponent_history[:-(n+1)]) ]
    
    possible_pattern = [ ''.join([ *opponent_history [-(n-1):], element ]) for element in ['S', 'R', 'P'] ]
    
    most_frequent = { k: pattern.count(k) for k in possible_pattern }

    predicted_choice = max(most_frequent, key = most_frequent.get)[-1]
    

    guess = winning_combinations [predicted_choice]
    
  
  return guess
  



           

      

    
  



