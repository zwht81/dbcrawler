<template>
  <div class="s_table_root">
    <v-app>
      <v-card class="s_table">
        <v-card-title>
          <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
            color="#00ACA5"
          ></v-text-field>
        </v-card-title>
        <v-data-table
          :headers="headers"
          :items="detailed"
          :search="search"
          :custom-filter="customFilter"
          @click:row="clickevent"
          :footer-props="{
            disableItemsPerPage: true,
            itemsPerPageOptions: [10],
          }"
          color="#00ACA5"
        >
          <template v-slot:[`item.nowcases`]="{ item }">
            <v-chip :color="getColor(item.nowcases)" dark>
              {{ item.nowcases }}
            </v-chip>
          </template>
        </v-data-table>
      </v-card>
    </v-app>
  </div>
</template>

<script>
var countryen2zh = require("../../data/utils/countryen2zh.json");
var provinceen2zh = require("../../data/utils/china_en2province.json");
var countryName = function (name) {
  // en2zh
  for (var key in countryen2zh) {
    if (countryen2zh[key]["value"] == name) return countryen2zh[key]["label"];
  }
  return name;
};
export default {
  name: "StatisticTable",
  props: {
    type: {
      type: String,
      required: true,
    },
    tableData: {
      type: Array,
      required: true,
    },
  },
  watch: {
    tableData() {
      this.loadData();
    },
  },
  mounted() {
    this.loadData();
  },

  data() {
    return {
      search: "",
      headers: [
        {
          text: "省份",
          align: "start",
          sortable: false,
          value: "zhname",
        },
        { text: "现有确诊", value: "nowcases" },
        { text: "累积确诊", value: "cases" },
        { text: "累积治愈", value: "recovered" },
        { text: "累积死亡", value: "deaths" },
      ],
      detailed: [],
    };
  },
  methods: {
    getColor(nowcases) {
      if (nowcases > 100000) return "red";
      else if (nowcases > 1000) return "orange";
      else return "green";
    },
    customFilter(_, search, item) {
      if (
        item.name.toLowerCase().indexOf(search.toLowerCase()) != -1 ||
        item.zhname.toLowerCase().indexOf(search.toLowerCase()) != -1
      )
        return true;
      return false;
    },
    loadData() {
      this.detailed = this.$props.tableData;
      var i;
      var item;
      if (this.$props.type == "China") {
        this.headers[0].text = "省份";
        for (i in this.detailed) {
          for (item in provinceen2zh) {
            if (provinceen2zh[item]["value"] == this.detailed[i]["name"]) {
              this.detailed[i]["zhname"] = provinceen2zh[item]["label"];
              break;
            }
          }
        }
      } else {
        this.headers[0].text = "国家";
        for (i in this.detailed) {
          this.detailed[i]["zhname"] = countryName(this.detailed[i]["name"]);
        }
      }
    },
    clickevent(value) {
      if (this.$props.type == "China") {
        const { href } = this.$router.resolve({
          path: "chinaanalysis",
          query: {
            name: value.name,
          },
        });
        window.open(href, "_blank");
      } else {
        if (value.name == "China") {
          const { href } = this.$router.resolve({
            path: "chinaanalysis",
          });
          window.open(href, "_blank");
        } else {
          const { href } = this.$router.resolve({
            path: "globalanalysis",
            query: {
              name: value.name,
            },
          });
          window.open(href, "_blank");
        }
      }
    },
  },
};
</script>

<style>
.s_table_root {
  padding: 10px;
  height: 670px;
  overflow: hidden;
}
.s_table th {
  font-size: 18px !important;
  white-space: nowrap !important;
}
.s_table td {
  font-size: 18px !important;
  white-space: nowrap !important;
}
</style>
