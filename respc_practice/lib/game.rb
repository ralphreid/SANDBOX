
class Game

  COMBINATIONS = {
    "rock" => "scissors",
    "paper" => "rock",
    "scissors" => "paper"
  }

  def play(choice)

    if COMBINATIONS.has_key?(choice)
      "#{choice} beats #{COMBINATIONS[choice]}"
    else
      "not valid, please select from rock paper scissors"
    end

  end
end
