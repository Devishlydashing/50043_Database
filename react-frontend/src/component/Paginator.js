import React from 'react';
import { Pagination } from 'semantic-ui-react'

const Paginator = () => (
    <div>
    <Pagination page={offset} totalPages={10} />
    </div>
)

export default Paginator;