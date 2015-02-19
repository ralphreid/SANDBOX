require "spec_helper"

describe Game do

  it "can be instantiated" do
    expect(Game.new).to be_a Game
  end

  describe '#play' do
    let(:game) {Game.new}

    it "takes an input and returns a winner" do
      expect(game.play("scissors")).to eq "scissors beats paper"
    end

    it "paper beats rock" do
      expect(game.play("paper")).to eq "paper beats rock"
    end

    context 'when the input is not one of the choices' do
      it 'returns a message asking for a valid input' do
        expect((game.play"foo")).to eq "not valid, please select from rock paper scissors"
      end
    end

  end

end
