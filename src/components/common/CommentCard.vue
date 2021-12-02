<template>
    <div class="commentRoot">
      <div class="commentUser">
        <el-avatar size=medium src="https://img2.baidu.com/it/u=153086019,155710187&fm=26&fmt=auto&gp=0.jpg"> </el-avatar>
        <div style="display: flex; flex-direction: column; text-align: left; margin-left: 5px; padding: 4px">
          <div style="font-size: small">
            {{ username }}
<!--            Mohamed Al Aufi-->
          </div>
          <div style="font-size: small; color: gray">
            {{ user_info }}
          </div>
        </div>
      </div>
        <div class="commentInfo">

          <div class="commentInfoItem" v-if="isAuthority" style="background-color:#D9D221; font-weight:bold;">
              <svg width="20px" height="20.00px" viewBox="0 0 1024 1024">
                <path fill="white" d="M511.5 81c22.108 0 44.217 8.434 61.08 25.3l77.944 77.947h107.59c47.71 0 86.38 38.674 86.38 86.38v107.59l74.204 74.204c33.736 33.733 33.736 88.426 0 122.16l-74.205 74.205v111.329c0 47.706-38.67 86.38-86.38 86.38H646.786l-74.205 74.204C555.716 937.566 533.608 946 511.5 946c-22.11 0-44.218-8.434-61.081-25.3l-74.205-74.205H268.626c-47.704 0-86.38-38.674-86.38-86.38V652.528l-77.944-77.947c-33.736-33.733-33.736-88.426 0-122.16l77.943-77.947V270.628c0-47.705 38.677-86.38 86.38-86.38h103.85l77.943-77.947C467.283 89.435 489.39 81 511.498 81z m160.077 343.217c-11.677-11.677-30.608-11.677-42.285 0L486.564 566.944l-61.54-59.428c-11.76-11.357-30.43-11.147-41.932 0.385l-0.347 0.353-0.01 0.01c-11.47 11.878-11.14 30.807 0.739 42.278l81.098 78.316a29.762 29.762 0 0 0 13.637 7.533c10.422 3.505 22.393 1.106 30.696-7.197l162.682-162.682c11.677-11.677 11.677-30.609 0-42.285z"/></svg>
              权威
          </div>

          <div class="commentInfoItem" v-else style="background-color:#666666;">
              <i class="el-icon-user-solid"></i>
              普通用户
          </div>

          <div class="commentInfoItem" style="background-color:#06a19c;">
            {{ time }}
          </div>

        </div>

        <div class="commentContent">
            {{ content }}
        </div>
    </div>
</template>

<script>

export default {
    name: "CommentCard",
    props: ['username', 'isAuthority', 'content', 'time', 'user_info']
}

</script>

<style scoped>
.commentRoot {
    padding: 20px;
    background-color: white;
    box-shadow: 0px 0px 10px 2px rgba(128, 128, 128, 0.2);
    border-radius: 5px;

    width: 100%;

    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
}
.commentUser {
    align-self: flex-start;
    display: flex;
    flex-direction: row;
    font-weight: bold;
}
.commentInfo {
    align-self: flex-start;

    display: flex;
    justify-content: center;
    align-items: center;
}
.commentInfoItem {

	color: white;
	border-radius: 5px;
	padding: 2px 12px 2px 12px;
	margin: 3px;
  height: 30px;
  display: flex;
  align-items: center;
}
.commentContent{
  margin-top: 10px;
  margin-left: 5px;
  font-size: 16px;
  text-align: left;
  width: 100%;
}

</style>
