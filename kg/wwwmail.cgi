#!/usr/local/bin/perl

#=====================================================================
# ���
#=====================================================================
#   ��    ��: WwwMail Ver3.26
#   �ŏI�X�V: 2002�N9��8��
#   �� �� ��: �m��X
#   ��    ��: �t���[�\�t�g�i���p�E���p���킸���p�E�����E���p�E�Ĕz�z�j
#   �� �V ��: http://tohoho.wakusei.ne.jp/

#=====================================================================
# �J�X�^�}�C�Y
#=====================================================================
# �� perl�̃p�X��
#    ���̃t�@�C���̐擪�̂P�s���A���Ȃ������p����T�[�o�[�ɃC���X�g�[
#    �����ꂽ perl �R�}���h�̃p�X���ɉ����ĕύX���Ă��������B�Ⴆ�΁A
#    �����������Ă��� BIGLOBE �ł́A#!/usr/local/bin/perl �ƂȂ�܂��B
#    ����Ȃ��ꍇ�́A�v���o�C�_��T�[�o�̊Ǘ��҂ɂ��₢���킹���������B
#   �u#!�v�̑O�ɂ́A�󕶎����s�⑼�̕������͂���Ȃ��悤�ɂ��Ă��������B

# �� ���M�惁�[���A�h���X
#    $mailto = 'abc@xxx.yyy.zzz'; �̂悤�ɂ��Ȃ��̃��[���A�h���X��
#    ���������Ă��������B
$mailto = 'minsyu.5@mis.janis.or.jp';

# �� �T�u�W�F�N�g(����)
#    ���M����郁�[���̃T�u�W�F�N�g���w�肵�Ă��������B
$subject = 'message from kato-gaku website';

# �� ���[�����M�R�}���h
#    Web�T�[�o�[��UNIX�̏ꍇ��sendmail�R�}���h�AWindows�n�̏ꍇ��BLATJ.EXE
#    �R�}���h�̃p�X�����w��i$mailcmd = 'C:\BLATJ\BLATJ.EXE'; �Ȃǁj���Ă�
#    �������B���̃R�}���h�����݂��Ȃ��ꍇ�́AWwwMail �͓��삵�܂���B�܂��A
#    ���݂��Ă��Ă��A���[�����M�̐ݒ肪�s���Ă��Ȃ��ꍇ������܂��B�ڍ�
#    �̓v���o�C�_��T�[�o�[�̊Ǘ��҂ɂ��₢���킹���������B
$mailcmd = '/usr/sbin/sendmail';

# �� ���M���ʃ��b�Z�[�W(�w�b�_)
#    <<END_OF_DATA �` END_OF_DATA �̊Ԃ��D�݂ɂ��킹�ĕύX���Ă��������B
$header = <<END_OF_DATA;
<html>
<head>
<meta http-equiv="Content-type" content="text/html; charset=Shift_JIS">
<title>���[�����M����</title>
</head>
<body>
<h1>���[�����M����</h1>
<hr>
<p>���L�̃��[���𑗐M���܂����B���肪�Ƃ��������܂����B</p>
<hr>
END_OF_DATA

# �� ���M���ʃ��b�Z�[�W(�t�b�^)
#    <<END_OF_DATA �` END_OF_DATA �̊Ԃ��D�݂ɂ��킹�ĕύX���Ă��������B
$footer = <<END_OF_DATA;
<hr>
<a href="/">[�߂�]</a>
</body>
</html>
END_OF_DATA

#====================================================================
# ���Ȑf�f�@�\�B
#====================================================================
# ���[�����M�����܂����삵�Ȃ����ɁA
# http://�`/�`/wwwmail.cgi?test �̌`���ŌĂяo���Ă��������B
if ($ENV{'REQUEST_METHOD'} eq "GET") {
	print "Content-type: text/html; charset=Shift_JIS\n";
	print "\n";
	print "<html>\n";
	print "<head>\n";
	print "<title>WwwMail���Ȑf�f</title>\n";
	print "</head>\n";
	print "<body>\n";
	print "<p>CGI�͐���ɓ��삵�Ă��܂��B</p>\n";
	unless (-f $mailcmd) {
		print "<p>$mailcmd ������܂���B</p>\n";
	}
	unless (-x $mailcmd) {
		print "<p>$mailcmd �����s�\�ł͂���܂���B</p>\n";
	}
	unless (-f "jcode.pl") {
		print "<p>jcode.pl ������܂���B</p>\n";
	}
	unless (-f "mimew.pl") {
		print "<p>mimew.pl ������܂���B</p>\n";
	}
	print "</body>\n";
	print "</html>\n";
	exit 0;
}

#====================================================================
# �{��
#====================================================================

#
# ���C�u�����̌Ăяo��
#
require "jcode.pl";
require "mimew.pl";

#
# ���͒l��ǂݎ��
#

	$host = $ENV{'REMOTE_HOST'};
	$addr = $ENV{'REMOTE_ADDR'};

	if ($host eq "" || $host eq $addr) {
		$host = gethostbyaddr(pack("C4", split(/\./, $addr)), 2) || $addr;
	}


if ($ENV{'REQUEST_METHOD'} eq "POST") {
	read(STDIN, $query_string, $ENV{'CONTENT_LENGTH'});
	@a = split(/&/, $query_string);
	foreach $x (@a) {
		($name, $value) = split(/=/, $x);
		$name =~ tr/+/ /;
		$name =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
		&jcode'convert(*name, "jis");
		$value =~ tr/+/ /;
		$value =~ s/%([0-9a-fA-F][0-9a-fA-F])/pack("C", hex($1))/eg;
		$value =~ s/[\r\n]+/\n/g;
		&jcode'convert(*value, "jis");
		if ($FORM{$name} eq "") {
			$FORM{$name} = $value;
			$FORM[$cnt++] = $name;
		} else {
			$FORM{$name} .= (" " . $value);
		}
	}
}

#
# EMAIL������ȃ��[�����ǂꂷ���ǂ������f����
#
if ($FORM{'EMAIL'} =~ /^[-_\.a-zA-Z0-9]+\@[-_\.a-zA-Z0-9]+$/) {
	$mailfrom = $FORM{'EMAIL'};
}

#
# ���[���w�b�_���쐬����
#
{
	&jcode'convert(*subject, "jis");
	$mailhead = "";
	$mailhead .= "Content-Type: text/plain; charset=\"iso-2022-jp\"\n";
	$mailhead .= "Content-Transfer-Encoding: 7bit\n";
	$mailhead .= "MIME-Version: 1.0\n";
	$mailhead .= "To: $mailto\n";
	if ($mailfrom) {
		$mailhead .= "From: $FORM{'EMAIL'}\n";
		$mailhead .= "Cc: $FORM{'EMAIL'}\n";
	} else {
		$mailhead .= "From: $mailto\n";
	}
	$mailhead .= "Subject: $subject\n";
	$mailhead .= "\n";
}

#
# ���[���{�f�B���쐬����
#
{
	for ($i = 0; $i < $cnt; $i++) {
		$mailbody .= "��$FORM[$i]\n$FORM{$FORM[$i]}\n";
	}

	$mailbody .= "$host\n";

	# "." �݂̂̍s�� ". " �ɕϊ�����B
	# 2��J��Ԃ��Ȃ��ƁA2�s�A���� "." �݂̂̍s�ɑΉ��ł��Ȃ�
	# "." �� ".." �ɕϊ����鏈������ʓI�����������A�����āA
	# "." �� ". " �ɕϊ�����B
	$mailbody =~ s/(^|\n)\.(\n|$)/$1. $2/g;
	$mailbody =~ s/(^|\n)\.(\n|$)/$1. $2/g;
}

#
# ���[���𑗐M����
#
if ($mailcmd =~ /sendmail/) {
	unless (open(OUT, "| $mailcmd -t")) {
		&errexit("���[���̑��M�Ɏ��s���܂����B(1)");
	}
	unless (print OUT &mimeencode($mailhead)) {
		&errexit("���[���̑��M�Ɏ��s���܂����B(2)");
	}
	unless (print OUT $mailbody) {
		&errexit("���[���̑��M�Ɏ��s���܂����B(3)");
	}
	close(OUT);
} elsif ($mailcmd =~ /BLAT/i) {
	&jcode'convert(*subject, "sjis");
	$cmd = "$mailcmd";
	$cmd .= " -";
	$cmd .= " -t $mailto";
	$cmd .= " -s \"$subject\"";
	if ($mailfrom) {
		$cmd .= " -c $mailfrom";
		$cmd .= " -f $mailfrom";
	}
	unless (open(OUT, "| $cmd > NUL:")) {
		&errexit("���[���̑��M�Ɏ��s���܂����B(4)");
	}
	&jcode'convert(*mailbody, "sjis");
	unless (print OUT $mailbody) {
		&errexit("���[���̑��M�Ɏ��s���܂����B(5)");
	}
	&jcode'convert(*mailbody, "jis");
	close(OUT);
} else {
	&errexit("���[�����M�R�}���h $mailcmd �����݂��܂���B");
}

#
# �u���E�U��ʂɑ��M���ʂ������o��
#
{
	&jcode'convert(*header, "sjis");
	&jcode'convert(*footer, "sjis");

	$mail = $mailhead . $mailbody;
	&jcode'convert(*mail, "euc");
	$mail =~ s/&/&amp;/g;
	$mail =~ s/"/&quot;/g;
	$mail =~ s/</&lt;/g;
	$mail =~ s/>/&gt;/g;
	$mail =~ s/\n/<BR>/g;
	&jcode'convert(*mail, "sjis");

	print "Content-type: text/html\n";
	print "\n";
	print "$header\n";
	print "$mail\n";
	print "$footer\n";
}

#
# �G���[���b�Z�[�W���o�͂��ďI��
#
sub errexit {
	local($err) = @_;
	local($msg);

	$msg  = "Content-type: text/html\n";
	$msg .= "\n";
	$msg .= "<html>\n";
	$msg .= "<head>\n";
	$msg .= "<meta http-equiv=\"Content-type\" content=\"text/html; charset=Shift_JIS\">\n";
	$msg .= "<title>���[�����M����</title>\n";
	$msg .= "</head>\n";
	$msg .= "<body>\n";
	$msg .= "<h1>���[�����M����</h1>\n";
	$msg .= "<hr>\n";
	$msg .= "<p>$err</p>\n";
	$msg .= "<p>�u���E�U�� [�߂�] �{�^���Ŗ߂��Ă��������B</p>\n";
	$msg .= "<hr>\n";
	$msg .= "</body>\n";
	$msg .= "</html>\n";

	&jcode'convert(*msg, "sjis");

	print $msg;

	exit(0);
}
