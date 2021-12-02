<template>
  <div class="forecast_root">
    <iframe :src="ruta" frameborder="no" class="forecast"></iframe>
  </div>
</template>

<script>
export default {
  name: "Forecast",
  components: {},
  data: () => ({
    ruta: "https://durian-forecast.herokuapp.com/",
  }),
  methods: {},
};
</script>

<style scoped>
.forecast_root {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  margin-top: 70px;
  margin-left: 50px;

}
.forecast {
  width: 100%;
  height: 700px;
  background-color: #565659;
}
</style>
