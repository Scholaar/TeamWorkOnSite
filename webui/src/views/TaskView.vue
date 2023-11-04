<template>
    <div class="container">
        <div class="main">
            <div class="btns">
                <el-button type="primary" @click="getTableData">刷新列表</el-button>
                <el-button type="primary" @click="sentAll">一键发送</el-button>
                <el-button type="danger" @click="deleteAll">清空任务</el-button>
            </div>
            <div class="table">
                <el-scrollbar height="85vh">
                    <el-table :data="tableData">
                        <!-- 选课时间	学号	姓名	课程名称	学分	百分成绩	五分成绩	考试类型	选修类型 -->
                        <!-- ['date', 'id', 'sname', 'cname', 'score', 'score_p', 'full_score', 'etype', 'stype'] -->
                        <el-table-column prop="date" label="选课时间"/>
                        <el-table-column prop="id" label="学号"/>
                        <el-table-column prop="sname" label="姓名"/>
                        <el-table-column prop="cname" label="课程名称"/>
                        <el-table-column prop="score" label="学分"/>
                        <el-table-column prop="score_p" label="百分成绩"/>
                        <el-table-column prop="full_score" label="五分成绩"/>
                        <el-table-column prop="etype" label="考试类型"/>
                        <el-table-column prop="stype" label="选修类型"/>
                        <el-table-column fixed="right" label="操作" width="170">
                            <template #default="scope">
                                <el-button
                                type="primary"
                                size="small"
                                @click="sent(scope.row.key)"
                                >发送</el-button>
                                <el-button
                                type="danger"
                                size="small"
                                @click="deleteTask(scope.row.key)"
                                >删除</el-button>
                            </template>
                        </el-table-column>
                    </el-table>
                </el-scrollbar>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import request from '../utils/requests'

const tableData = ref([])
const getTableData = async () => {
    const res = await request({
        url: '/api/data',
        method: 'get'
    })
    tableData.value = res.data.data
    console.log(res.data)
}

const sent = async (key) => {
    const res = await request({
        url: '/api/sent/' + key,
        method: 'get'
    })
    console.log(res.data)
    console.log(key)
}

const deleteTask = async (key) => {
    const res = await request({
        url: '/api/delete/' + key,
        method: 'get'
    })
    console.log(res.data)
    console.log(key)
}

const sentAll = async () => {
    const res = await request({
        url: '/api/sentAll',
        method: 'get'
    })
    console.log(res.data)
}

const deleteAll = async () => {
    const res = await request({
        url: '/api/deleteAll',
        method: 'get'
    })
    console.log(res.data)
}

onMounted(() => {
    getTableData()
})
</script>

<style lang="less" scoped>
.container{
//   background-color: antiquewhite;
  flex: 1 1;
  .main{
    // background-color: rgb(221, 240, 240);
    padding: 25px;
    height: 100%;
    .btns{
        display: flex;
        justify-content: flex-end;
    }
  }
}
</style>