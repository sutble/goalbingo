<script>
	import GoalList from "./components/GoalList.svelte";
	import Grid from "./components/Grid.svelte";

	let goalMap = {}
	function  handleGoalListMessage(event){
		goalMap = event.detail.goalMap
	}
</script>


<style>
	.app-container {
		display: flex;
  		flex-direction: row;
	}

	@media print {
		.instructions-container {
			display: none !important;
		}

	}

</style>


<div class="container">
	<div class="instructions-container">
		<h1>Bingo Goals Organizer</h1>
		<p>
		1. Write out 25 concrete actions you would like to take (hardest to easiest) 	<br>
		2. Drag and drop to rearrange the order of the goals <br>
		3. Copy over the grid into your journal <br>
		4. Throughout the month, cross out any goals you accomplish and try to get bingo! <br> <br>
		<b>Each row/column/diagonal in the grid will be the same difficulty (proven by math)</b>

		</p>
		<h3>Tips</h3>
		<p>	
		Pick action based goals that can be quantified ("Getting in shape" vs "Going to the gym 3 times in a week") <br>
		Dont feel pressured to fill out the entire list, any blanks become free spaces :) 	<br>
		Feel free to repeat the same goal multiple times (3 boxes say "Drink a veggie smoothie") <br> <br>
		Inspired by <a href='https://www.reddit.com/r/bulletjournal/comments/ssteux/bingo_helped_me_crush_my_6month_goals_in_6weeks/'>this reddit post</a><br>
		</p>
		<hr>
		<br>
	</div>
	<div class="app-container">
		<div class="goal-list-container">
				<GoalList on:updatedGoals={handleGoalListMessage}></GoalList>
		</div>
		<div class="grid-container">
			<Grid goalMap={goalMap}/>
		</div>
		
	</div>
</div>