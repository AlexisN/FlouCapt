<?php
/**
*	FlouCapt process_form.php
*	https://github.com/AlexisN/FlouCapt
*
*	@author Bannier Kevin, Thomas Mathieu, Nicol Alexis
*/
$form = new ProcessForm();
$form->field_rules = array(
    'field1'=>'required',
    'field2'=>'required',
    'field3'=>'number|required',
    'field4'=>'required',
    'field5'=>'required',
    'field6'=>'required',
    'field7'=>'required',
    'field8'=>'required',
    'field9'=>'required'
    );
$form->validate();

class ProcessForm
{
    public $field_rules;
    public $error_messages;
    public $fields;
    private $error_list;
    private $is_xhr;

    function __construct()
    {
        $this->error_messages = array(
'required' => 'This field is required', //Error message for input required
'number' => 'Please enter a numeric value',//Error message for numeric value
);

        $this->field_rules = array();
        $this->error_list = '';
        $this->fields = $_POST;
        $this->is_xhr = $this->xhr();
    }

    function validate()
    {
        if (!empty($this->fields))
        {
//Validate each of the fields
            foreach ($this->field_rules as $field => $rules)
            {
                $rules = explode('|', $rules);

                foreach ($rules as $rule)
                {
                    $result = null;

                    if (isset($this->fields[$field]))
                    {
                        $param = false;

                        if (preg_match("/(.*?)\[(.*?)\]/", $rule, $match))
                        {
                            $rule = $match[1];
                            $param = $match[2];
                        }

                        $this->fields[$field] = $this->clean($this->fields[$field]);

//if the field is a checkbox group create string
                        if (is_array($this->fields[$field]))
                            $this->fields[$field] = implode(', ', $this->fields[$field]);

// Call the function that corresponds to the rule
                        if (!empty($rule))
                            $result = $this->$rule($this->fields[$field], $param);

// Handle errors
                        if ($result === false)
                            $this->set_error($field, $rule);
                    }
                }
            }

            if (empty($this->error_list))
            {
                if ($this->is_xhr)
                    echo json_encode(array('status' => 'success'));

                $this->process();
            }
            else
            {
                if ($this->is_xhr)
                    echo json_encode(array('status' => 'invalid', 'errors' => $this->error_list));
                else echo $this->error_list;
            }
        }
    }

    /** Execution if form it's good */
    function process()
    {

//Configuration config file web application
        $mdp = $_POST['mdp'];
        $name = $_POST['onglet'];
        $adOne = $_POST['ad'];
        $adOneL= $_POST['adL'];
        $adTwo = $_POST['adTwo'];
        $adTwoL = $_POST['adTwoL'];
        $adV = $_POST['adV'];
        $adVL=strlen($adV);
        $adI = $_POST['adI'];
        $adIL=strlen($adV);
        $about = $_POST['about'];
        $fOne = fopen("/etc/floucapt/webConf.ini", "w+");
        fwrite($fOne, $mdp."\n");
        fwrite($fOne, $name."\n");
        fwrite($fOne, $adOne."\n");
        fwrite($fOne, $adOneL."\n");
        fwrite($fOne, $adTwo."\n");
        fwrite($fOne, $adTwoL."\n");
        fwrite($fOne, $adV."\n");
        fwrite($fOne, $adI."\n");
        fwrite($fOne, $about);
        fclose($fOne);

    //Configuration config file python application
        $reader = file('/etc/floucapt/config.ini');
        $line =  $reader[3];

        $link = $_POST['link'];
        $frequency = $_POST['frequency'];
        $fTwo = fopen("cfg.txt", "w+");
        fwrite($fTwo, "[DEFAULT]\n");
        fwrite($fTwo, "frequencyPictures =".$frequency."\n");
        fwrite($fTwo, "link =".$link."\n");
        fwrite($fTwo, $line);
        fclose($fTwo);



    }

    /** Error view function */
    function set_error($field, $rule)
    {
        if ($this->is_xhr)
        {
            $this->error_list[$field] = $this->error_messages[$rule];
        }
        else $this->error_list .= "<div class='error'>$field: " . $this->error_messages[$rule] . "</div>";
    }


    function xhr()
    {
        return (!empty($_SERVER['HTTP_X_REQUESTED_WITH']) && strtolower($_SERVER['HTTP_X_REQUESTED_WITH']) == 'xmlhttprequest') ? true : false;
    }


    /** Validation Functions */
    function required($str, $val = false)
    {

        if (!is_array($str))
        {
            $str = trim($str);
            return ($str == '') ? false : true;
        }
        else
        {
            return (!empty($str));
        }
    }
    /** Test if a number */
    function number($str)
    {
        return (!is_numeric($str)) ? false : true;
    }


    /** clean form */
    function clean($str)
    {
        $str = is_array($str) ? array_map(array("ProcessForm", 'clean'), $str) : str_replace('\\', '\\\\', strip_tags(trim(htmlspecialchars((get_magic_quotes_gpc() ? stripslashes($str) : $str), ENT_QUOTES))));
        return $str;
    }
}


?>
