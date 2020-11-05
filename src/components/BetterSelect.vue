<template>
    <div>
        <div>
            <b-form-input
                class='search-input'
                type='search'
                v-model='filterCriteria'
                v-on:click='toggleDropDown()'
                v-on:keyup.enter='selectItem()'
                :placeholder='placeholder'>
            </b-form-input>
        </div>
        <div>
            <b-collapse id='drop-down'>
                <b-table
                    no-border-collapse
                    ref='collapsibleTable'
                    responsive='sm'
                    selectable
                    select-mode='single'
                    sticky-header='200px'
                    thead-class='d-none'
                    v-model='filteredRows'
                    :fields='fields'
                    :filter='filterCriteria'
                    :items='items'
                    :sort-by.sync='sortBy'
                    :sort-desc.sync='sortDesc'
                    @row-selected='rowSelected'>
                </b-table>
            </b-collapse>
        </div>
    </div>
</template>

<script>

export default {
    data() {
        return {
            filterCriteria: '',
            filteredRows: []
        }
    },
    methods: {
        toggleDropDown() {
            this.$root.$emit('bv::toggle::collapse', 'drop-down')
        },
        selectItem() {
            if (this.filteredRows.length === 1) {
                this.$refs.collapsibleTable.selectRow(0)
            }
        },
        rowSelected(rowArray) {
            // No rows or 1 row can be selected
            if (rowArray.length === 1) {
                this.$emit('item-selected', rowArray[0])
                this.filterCriteria = rowArray[0][this.display]
                this.toggleDropDown()
            }
        }
    },
    props: {
        display: {
            required: true,
            type: String
        },
        fields: {
            required: true,
            type: Array
        },
        items: {
            required: true,
            type: Array
        },
        placeholder: {
            required: false,
            default: 'Select'
        },
        sortBy: {
            required: true,
            type: String
        },
        sortDec: {
            default: false,
            required: false
        }
    }
}
</script>