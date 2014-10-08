function multipart_build_query($fields)
{
    $boundary = md5(time());
    $data = '';
    foreach ($fields as $field) {
        // add boundary
        $data .= '--' . $boundary . "\r\n";
        // add headers
        foreach ($field['headers'] as $header => $value) {
            $data .= $header . ': ' . $value . "\r\n";
        }
        // add blank line
        $data .= "\r\n";

        // add body
        $data .= $field['body'] . "\r\n";
    }
    // add closing boundary if there where fields
    if ($data) {
        $data .= $data .= '--' . $boundary . "--\r\n";
    }
    return $data;
}