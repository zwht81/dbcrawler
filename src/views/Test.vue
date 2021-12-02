<template>
	<div class="root">
		<h1 style='margin-top:100px;'>This is Test Page</h1>

		<airline-detail ref="AirlineDetail"></airline-detail>
	</div>
</template>

<script>
import AirlineDetail from "../components/AirlineDetail";
export default {
	name: 'Test',
	components: {
		AirlineDetail,
	},
}
</script>

<style>

</style>
