require_relative 'project'

describe Project do
  
  before do
    @initial_funds = 1000
    @project = Project.new("Project ABC", 5000, @initial_funds)
    $stdout = StringIO.new
  end
  
  it "has an initial target funding amount" do
    @project.target.should == 5000
  end
  
  it "computes the total funds outstanding as the target funding amount minus the funding amount" do    
    @project.total_funding_outstanding.should == (5000 - 1000)
  end

  it "increases funds by 25 when funds are added" do
    @project.add_funds
    
    @project.funding.should == @initial_funds + 25
  end
  
  it "decreases funds by 15 when funds are removed" do
    @project.remove_funds
    
    @project.funding.should == @initial_funds - 15
  end

  context "created without a funding amount" do
    before do
      @project = Project.new("Project ABC", 5000)
    end
    
    it "has a default funding amount of 0" do
      @project.funding.should == 0
    end
  end

end