<template>
  <section class="section">
    <b-table
      :data="aiAnalysisLog"
      :columns="columns"
      :loading="isLoading"
      striped
      bordered>
      <template #empty v-if="aiAnalysisLog.length === 0">
        <div class="has-text-centered">データがありません。</div>
      </template>
    </b-table>
  </section>
</template>

<script>
export default {
  name: 'LogTable',
  props: {
    aiAnalysisLog: {
      type: Array,
      require: true
    },
    loadingStatus: {
      type: String,
      require: true
    },
  },
  computed: {
    isLoading () {
      return this.loadingStatus === 'get'
    },
    aiAnalysisLogFilter () {
      return this.aiAnalysisLog.map(
        (v) => {
          let record = v
          record.image_path = process.env + v.image_path
          return record
        }
      )
    }
  },
  data () {
    return {
      columns: [
        {
            field: 'id',
            label: 'ID',
            width: '40',
            numeric: true
        },
        {
            field: 'image_path',
            label: '画像のパス',
        },
        {
            field: 'success',
            label: '成功可否',
            width: '90',
        },
        {
            field: 'message',
            label: 'メッセージ',
            width: '120',
        },
        {
            field: '_class',
            label: '分類結果',
            width: '90'
        },
        {
            field: 'confidence',
            label: '信頼度',
            width: '75'
        },
        {
            field: 'request_timestamp',
            label: 'リクエスト日時',
        },
        {
            field: 'response_timestamp',
            label: 'レスポンス日時',
        }
      ]
    }
  },
}
</script>
<style scoped>
</style>