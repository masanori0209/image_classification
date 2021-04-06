<template>
  <section class="section">
    <b-table
      :data="aiAnalysisLog"
      :columns="columns"
      :loading="isLoading"
      striped
      bordered>
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