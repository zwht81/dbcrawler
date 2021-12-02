<template>
	<div class="row">
		<div class="trackInfo">
			<svg width="40px"
                height="35px"
                style="transform: rotate(90deg)"
                viewBox="0 0 1000 1000"><path fill="#666666" d="M796.014 412.647l-257.492-257.492c-20.11-20.11-52.709-20.11-72.819 0l-257.492 257.492c-20.11 20.11-20.11 52.709 0 72.819s52.709 20.11 72.819 0l169.585-169.585v493.664c0 28.453 23.046 51.499 51.499 51.499s51.499-23.046 51.499-51.499v-493.664l169.585 169.585c10.042 10.043 23.226 15.089 36.41 15.089s26.367-5.021 36.41-15.089c20.11-20.11 20.11-52.709 0-72.819z" /></svg>
		</div>
		
		<div >
			<div class="trackCity">
				{{destination}}
			</div>
		</div>
    </div>	
</template>

<script>
export default {
	name: "trackCard",
	props: [ 'destination'],
}
</script>

<style scoped>
.trackCardRoot {
	border: #bfbec0 solid thin;
	border-radius: 30px;
	width: auto;
	height: 120px;
	
	position: relative;
	
	display: flex;
	align-items: center;
	justify-content: space-around;

	white-space: nowrap;
}
.trackTime {
/* 	position: absolute;
	top: 3px;
	left: 15px; */
	
	font-size: 15px;
	font-weight: 500;
	
	color: #434344;
	
	position: relative;
	bottom: 5px;
}
.trackCity {
	font-size: 40px;
	font-weight: bold;
	
	white-space: nowrap;
	text-align: center;
	
	font-size: 27px;
	font-weight: 500;
	
	background-color: #e6e6e6;
	
	border-radius: 30px;
	
	padding: 5px 15px 5px 15px;
	margin: 3px;
}
.trackNum {
	white-space: nowrap;
	text-align: center;
	
	font-size: 17px;
	font-weight: 500;
	
	background-color: #06a19c;
	color: white;
	
	border-radius: 30px;
	
	padding: 2px 10px 0px 10px;
	
	position: relative;
	top: 3px;
}
.row {
    display: flex;
    flex-direction: row;
}
.trackInfo {
    margin-top: 10px;
}
</style>
